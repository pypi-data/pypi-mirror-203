"""Settings Controller Module"""
__docformat__ = "numpy"

# IMPORTATION STANDARD
import argparse
import logging
import os
import os.path
from pathlib import Path
from typing import List, Optional, Union

# IMPORTATION THIRDPARTY
import pytz

import openbb_terminal.core.session.hub_model as Hub
from openbb_terminal import theme

# IMPORTATION INTERNAL
from openbb_terminal.core.config.paths import (
    I18N_DICT_LOCATION,
    SETTINGS_ENV_FILE,
    STYLES_DIRECTORY_REPO,
)
from openbb_terminal.core.session.constants import CHARTS_TABLES_URL, COLORS_URL
from openbb_terminal.core.session.current_user import (
    get_current_user,
    is_local,
    set_preference,
)
from openbb_terminal.core.session.env_handler import write_to_dotenv
from openbb_terminal.custom_prompt_toolkit import NestedCompleter
from openbb_terminal.decorators import log_start_end
from openbb_terminal.helper_funcs import (
    AVAILABLE_FLAIRS,
    check_positive,
    get_flair,
    get_user_timezone_or_invalid,
    parse_and_split_input,
)
from openbb_terminal.menu import session
from openbb_terminal.parent_classes import BaseController
from openbb_terminal.rich_config import RICH_TAGS, MenuText, console

# pylint: disable=too-many-lines,no-member,too-many-public-methods,C0302
# pylint: disable=import-outside-toplevel

logger = logging.getLogger(__name__)


class SettingsController(BaseController):
    """Settings Controller class"""

    CHOICES_COMMANDS: List[str] = [
        "chart",
        "colors",
        "dt",
        "flair",
        "height",
        "lang",
        "table",
        "tbnews",
        "tweetnews",
        "tz",
        "userdata",
        "width",
    ]
    if is_local():
        CHOICES_COMMANDS.append("source")
    PATH = "/settings/"
    CHOICES_GENERATION = True

    languages_available = [
        lang.strip(".yml")
        for lang in os.listdir(I18N_DICT_LOCATION)
        if lang.endswith(".yml")
    ]

    def __init__(
        self, queue: Optional[List[str]] = None, env_file: str = str(SETTINGS_ENV_FILE)
    ):
        """Constructor"""
        super().__init__(queue)
        self.env_file = env_file

        if session and get_current_user().preferences.USE_PROMPT_TOOLKIT:
            choices: dict = self.choices_default
            choices["tz"] = {c: None for c in pytz.all_timezones}
            choices["lang"] = {c: None for c in self.languages_available}
            choices["flair"]["--emoji"] = {c: None for c in AVAILABLE_FLAIRS}
            choices["flair"]["-e"] = "--emoji"

            self.choices = choices
            self.completer = NestedCompleter.from_nested_dict(choices)

        self.sort_filter = r"((tz\ -t |tz ).*?("
        for tz in pytz.all_timezones:
            tz = tz.replace("/", r"\/")
            self.sort_filter += f"{tz}|"
        self.sort_filter += ")*)"

        self.PREVIEW = ", ".join(
            [
                f"[{tag}]{tag}[/{tag}]"
                for tag in sorted(
                    set(
                        name.replace("[", "").replace("]", "").replace("/", "")
                        for name in RICH_TAGS
                    )
                )
            ]
        )

    def parse_input(self, an_input: str) -> List:
        """Parse controller input

        Overrides the parent class function to handle github org/repo path convention.
        See `BaseController.parse_input()` for details.
        """
        # Filtering out
        sort_filter = self.sort_filter

        custom_filters = [sort_filter]

        commands = parse_and_split_input(
            an_input=an_input, custom_filters=custom_filters
        )
        return commands

    def print_help(self):
        """Print help"""
        current_user = get_current_user()

        mt = MenuText("settings/")
        mt.add_info("_info_")
        mt.add_raw("\n")
        mt.add_setting("dt", current_user.preferences.USE_DATETIME)
        mt.add_raw("\n")
        mt.add_cmd("chart")
        mt.add_raw("\n")
        mt.add_param("_chart", current_user.preferences.CHART_STYLE)
        mt.add_raw("\n")
        mt.add_cmd("table")
        mt.add_raw("\n")
        mt.add_param("_table", current_user.preferences.TABLE_STYLE)
        mt.add_raw("\n")
        mt.add_cmd("colors")
        mt.add_raw("\n")
        mt.add_param(
            "_colors", f"{current_user.preferences.RICH_STYLE} -> {self.PREVIEW}"
        )
        mt.add_raw("\n")
        mt.add_cmd("flair")
        mt.add_raw("\n")
        mt.add_param("_flair", get_flair())
        mt.add_raw("\n")
        mt.add_cmd("lang")
        mt.add_raw("\n")
        mt.add_param("_language", current_user.preferences.USE_LANGUAGE)
        mt.add_raw("\n")
        mt.add_cmd("userdata")
        mt.add_raw("\n")
        mt.add_param(
            "_user_data_folder",
            current_user.preferences.USER_DATA_DIRECTORY,
        )
        mt.add_raw("\n")
        mt.add_cmd("tz")
        mt.add_raw("\n")
        mt.add_param("_timezone", get_user_timezone_or_invalid())
        mt.add_raw("\n")
        mt.add_cmd("height")
        mt.add_cmd("width")
        mt.add_raw("\n")
        mt.add_param("_plot_height", current_user.preferences.PLOT_PYWRY_HEIGHT, 12)
        mt.add_param("_plot_width", current_user.preferences.PLOT_PYWRY_WIDTH, 12)
        mt.add_raw("\n")
        if is_local():
            mt.add_cmd("source")
            mt.add_raw("\n")
            mt.add_param(
                "_data_source",
                get_current_user().preferences.USER_DATA_SOURCES_FILE,
            )
            mt.add_raw("\n")
        mt.add_setting("tbnews", current_user.preferences.TOOLBAR_TWEET_NEWS)
        if current_user.preferences.TOOLBAR_TWEET_NEWS:
            mt.add_raw("\n")
            mt.add_cmd("tweetnews")
            mt.add_raw("\n")
            mt.add_param(
                "_tbnu",
                current_user.preferences.TOOLBAR_TWEET_NEWS_SECONDS_BETWEEN_UPDATES,
            )
            mt.add_param(
                "_nttli",
                current_user.preferences.TOOLBAR_TWEET_NEWS_NUM_LAST_TWEETS_TO_READ,
            )
            mt.add_param(
                "_tatt", current_user.preferences.TOOLBAR_TWEET_NEWS_ACCOUNTS_TO_TRACK
            )
            mt.add_param("_tk", current_user.preferences.TOOLBAR_TWEET_NEWS_KEYWORDS)
        console.print(text=mt.menu_text, menu="Settings")

    @staticmethod
    def set_and_save_preference(name: str, value: Union[bool, Path, str]):
        """Set preference and write to .env

        Parameters
        ----------
        name : str
            Preference name
        value : Union[bool, Path, str]
            Preference value
        """
        set_preference(name, value)
        write_to_dotenv("OPENBB_" + name, str(value))

    @log_start_end(log=logger)
    def call_dt(self, other_args: List[str]):
        """Process dt command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="dt",
            description="Set the use of datetime in the plots",
        )
        ns_parser = self.parse_simple_args(parser, other_args)
        if ns_parser:
            self.set_and_save_preference(
                "USE_DATETIME", not get_current_user().preferences.USE_DATETIME
            )

    @log_start_end(log=logger)
    def call_colors(self, other_args: List[str]):
        """Process colors command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="colors",
            description="Console style.",
        )
        theme.load_available_styles()
        parser.add_argument(
            "-s",
            "--style",
            type=str,
            choices=theme.console_styles_available,
            dest="style",
            required="-h" not in other_args and "--help" not in other_args,
            help="To use 'custom' option, go to https://openbb.co/customize and create your theme."
            " Then, place the downloaded file 'openbb_config.richstyle.json'"
            f" inside {get_current_user().preferences.USER_STYLES_DIRECTORY} or "
            f"{STYLES_DIRECTORY_REPO}. If you have a hub account you can change colors "
            f"here {COLORS_URL}.",
        )
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "-s")
        ns_parser = self.parse_simple_args(parser, other_args)
        if ns_parser:
            if is_local():
                self.set_and_save_preference("RICH_STYLE", ns_parser.style)
            else:
                set_preference("RICH_STYLE", ns_parser.style)
                Hub.upload_config(
                    key="RICH_STYLE",
                    value=ns_parser.style,
                    type_="settings",
                    auth_header=get_current_user().profile.get_auth_header(),
                )
                console.print("")
            console.print("Colors updated.")

    @log_start_end(log=logger)
    def call_chart(self, other_args: List[str]):
        """Process chart command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="theme",
            description="Choose chart style.",
        )
        parser.add_argument(
            "-s",
            "--style",
            type=str,
            dest="style",
            choices=["dark", "light"],
            help="Choose chart style. If you have a hub account you can change theme "
            f"here {CHARTS_TABLES_URL}.",
            required="-h" not in other_args and "--help" not in other_args,
        )
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "-s")
        ns_parser = self.parse_simple_args(parser, other_args)
        if ns_parser and ns_parser.style:
            if is_local():
                self.set_and_save_preference("CHART_STYLE", ns_parser.style)
            else:
                set_preference("CHART_STYLE", ns_parser.style)
                Hub.upload_config(
                    key="chart",
                    value=ns_parser.style,
                    type_="terminal_style",
                    auth_header=get_current_user().profile.get_auth_header(),
                )
                console.print("")
            console.print("Chart theme updated.\n")

    @log_start_end(log=logger)
    def call_table(self, other_args: List[str]):
        """Process theme command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="theme",
            description="Choose table style.",
        )
        parser.add_argument(
            "-s",
            "--style",
            type=str,
            dest="style",
            choices=["dark", "light"],
            help="Choose table style. If you have a hub account you can change theme "
            f"here {CHARTS_TABLES_URL}.",
            required="-h" not in other_args and "--help" not in other_args,
        )
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "-s")
        ns_parser = self.parse_simple_args(parser, other_args)
        if ns_parser and ns_parser.style:
            if is_local():
                self.set_and_save_preference("TABLE_STYLE", ns_parser.style)
            else:
                set_preference("TABLE_STYLE", ns_parser.style)
                Hub.upload_config(
                    key="table",
                    value=ns_parser.style,
                    type_="terminal_style",
                    auth_header=get_current_user().profile.get_auth_header(),
                )
                console.print("")
            console.print("Table theme updated.\n")

    @log_start_end(log=logger)
    def call_source(self, other_args: List[str]):
        """Process source command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="source",
            description="Preferred data source file.",
        )
        parser.add_argument(
            "-f",
            "--file",
            type=str,
            dest="file",
            help="file",
        )
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "-f")
        ns_parser = self.parse_simple_args(parser, other_args)
        if ns_parser and ns_parser.file:
            if os.path.exists(ns_parser.file):
                self.set_and_save_preference(
                    "USER_DATA_SOURCES_FILE", str(ns_parser.file)
                )
                console.print("[green]Sources file changed successfully![/green]")
            else:
                console.print("[red]Couldn't find the sources file![/red]")

    @log_start_end(log=logger)
    def call_height(self, other_args: List[str]):
        """Process height command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="height",
            description="select plot height (autoscaling disabled)",
        )
        parser.add_argument(
            "-v",
            "--value",
            type=int,
            dest="value",
            help="value",
            required="-h" not in other_args,
        )
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "-v")
        ns_parser = self.parse_simple_args(parser, other_args)
        if ns_parser:
            self.set_and_save_preference("PLOT_PYWRY_HEIGHT", ns_parser.value)

    @log_start_end(log=logger)
    def call_width(self, other_args: List[str]):
        """Process width command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="width",
            description="select plot width (autoscaling disabled)",
        )
        parser.add_argument(
            "-v",
            "--value",
            type=int,
            dest="value",
            help="value",
            required="-h" not in other_args,
        )
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "-v")
        ns_parser = self.parse_simple_args(parser, other_args)
        if ns_parser:
            self.set_and_save_preference("PLOT_PYWRY_WIDTH", ns_parser.value)

    @log_start_end(log=logger)
    def call_lang(self, other_args: List[str]):
        """Process lang command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="lang",
            description="Choose language for terminal",
        )
        parser.add_argument(
            "-v",
            "--value",
            type=str,
            dest="value",
            help="Language",
            choices=self.languages_available,
            default="",
        )
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "-v")
        ns_parser = self.parse_simple_args(parser, other_args)
        if ns_parser:
            if ns_parser.value:
                self.set_and_save_preference("USE_LANGUAGE", ns_parser.value)
            else:
                console.print(
                    f"Languages available: {', '.join(self.languages_available)}"
                )

    @log_start_end(log=logger)
    def call_tz(self, other_args: List[str]):
        """Process tz command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            description="""
                   Setting a different timezone
               """,
        )
        parser.add_argument(
            "-t",
            dest="timezone",
            help="Choose timezone",
            required="-h" not in other_args,
            metavar="TIMEZONE",
            choices=pytz.all_timezones,
        )

        if other_args and "-t" not in other_args[0]:
            other_args.insert(0, "-t")

        ns_parser = self.parse_simple_args(parser, other_args)
        if ns_parser and ns_parser.timezone:
            self.set_and_save_preference("TIMEZONE", ns_parser.timezone)

    @log_start_end(log=logger)
    def call_flair(self, other_args: List[str]):
        """Process flair command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="flair",
            description="set the flair emoji to be used",
        )
        parser.add_argument(
            "-e",
            "--emoji",
            type=str,
            dest="emoji",
            help="flair emoji to be used",
            nargs="+",
        )
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "-e")
        ns_parser = self.parse_simple_args(parser, other_args)
        if ns_parser:
            if not ns_parser.emoji:
                ns_parser.emoji = ""
            else:
                ns_parser.emoji = " ".join(ns_parser.emoji)

            self.set_and_save_preference("FLAIR", ns_parser.emoji)

    @log_start_end(log=logger)
    def call_userdata(self, other_args: List[str]):
        """Process userdata command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="userdata",
            description="Set folder to store user data such as exports, presets, logs",
        )
        parser.add_argument(
            "--folder",
            type=str,
            dest="folder",
            help="Folder where to store user data. ",
            default=f"{str(Path.home() / 'OpenBBUserData')}",
        )
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "--folder")
        ns_parser = self.parse_simple_args(parser, other_args)

        if ns_parser and (other_args or self.queue):
            userdata_path = "" if other_args else "/"

            userdata_path += "/".join([ns_parser.folder] + self.queue)
            self.queue = []

            userdata_path = userdata_path.replace("'", "").replace('"', "")

            default_path = Path.home() / "OpenBBUserData"

            success_userdata = False
            while not success_userdata:
                if userdata_path.upper() == "DEFAULT":
                    console.print(
                        f"User data to be saved in the default folder: '{default_path}'"
                    )
                    self.set_and_save_preference("USER_DATA_DIRECTORY", default_path)
                    success_userdata = True
                else:
                    # If the path selected does not start from the user root, give relative location from root
                    if userdata_path[0] == "~":
                        userdata_path = userdata_path.replace(
                            "~", os.path.expanduser("~")
                        )

                    # Check if the directory exists
                    if os.path.isdir(userdata_path):
                        console.print(
                            f"User data to be saved in the selected folder: '{userdata_path}'"
                        )
                        self.set_and_save_preference(
                            "USER_DATA_DIRECTORY", userdata_path
                        )
                        success_userdata = True
                    else:
                        console.print(
                            "[red]The path selected to user data does not exist![/red]\n"
                        )
                        user_opt = "None"
                        while user_opt not in ("Y", "N"):
                            user_opt = input(
                                f"Do you wish to create folder: `{userdata_path}` ? [Y/N]\n"
                            ).upper()

                        if user_opt == "Y":
                            os.makedirs(userdata_path)
                            console.print(
                                f"[green]Folder '{userdata_path}' successfully created.[/green]"
                            )
                            self.set_and_save_preference(
                                "USER_DATA_DIRECTORY", userdata_path
                            )
                        else:
                            # Do not update userdata_folder path since we will keep the same as before
                            console.print(
                                "[yellow]User data to keep being saved in "
                                + "the selected folder: "
                                + f"{str(get_current_user().preferences.USER_DATA_DIRECTORY)}[/yellow]"
                            )
                        success_userdata = True

        console.print()

    @log_start_end(log=logger)
    def call_tbnews(self, other_args):
        """Process tbnews command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="tweetnews",
            description="Tweak tweet news toolbal parameters",
        )
        ns_parser = self.parse_known_args_and_warn(parser, other_args)
        if ns_parser:
            current_user = get_current_user()
            if current_user.preferences.TOOLBAR_TWEET_NEWS:
                console.print("Will take effect when running terminal next.")
            self.set_and_save_preference(
                "TOOLBAR_TWEET_NEWS",
                not get_current_user().preferences.TOOLBAR_TWEET_NEWS,
            )

    @log_start_end(log=logger)
    def call_tweetnews(self, other_args: List[str]):
        """Process tweetnews command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="tweetnews",
            description="Tweak tweet news parameters",
        )
        parser.add_argument(
            "-t",
            "--time",
            type=check_positive,
            required=False,
            dest="time",
            help="Time (in seconds) between tweet news updates, e.g. 300",
        )
        parser.add_argument(
            "-a",
            "--accounts",
            type=str,
            required=False,
            dest="accounts",
            help="Twitter accounts to track news separated by commmas."
            "For instance: 'WatcherGuru,unusual_whales,gurgavin'",
        )
        parser.add_argument(
            "-k",
            "--keywords",
            type=str,
            required=False,
            dest="keywords",
            nargs="+",
            help="Keywords to look for, separated by commmas."
            "For instance: 'Just In, Breaking'",
        )
        parser.add_argument(
            "-n",
            "--number",
            type=check_positive,
            required=False,
            dest="number",
            help="Number of tweets to look into from each account, e.g. 3",
        )
        ns_parser = self.parse_known_args_and_warn(parser, other_args)
        if ns_parser:
            if ns_parser.time:
                self.set_and_save_preference(
                    "TOOLBAR_TWEET_NEWS_SECONDS_BETWEEN_UPDATES",
                    str(ns_parser.time),
                )

            if ns_parser.number:
                self.set_and_save_preference(
                    "TOOLBAR_TWEET_NEWS_NUM_LAST_TWEETS_TO_READ",
                    str(ns_parser.number),
                )

            if ns_parser.accounts:
                self.set_and_save_preference(
                    "TOOLBAR_TWEET_NEWS_ACCOUNTS_TO_TRACK",
                    str(ns_parser.accounts),
                )

            if ns_parser.keywords:
                self.set_and_save_preference(
                    "TOOLBAR_TWEET_NEWS_KEYWORDS",
                    str(" ".join(ns_parser.keywords)),
                )
