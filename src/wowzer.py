
import main


APP_NAME = 'wowzer'
APP_VERSION = '0.0.1'
AUTHOR = 'Frank Pereny'
COPYRIGHT_YEAR = '2022'
WEBSITE_LINK = 'https://github.com/fjpereny/wowzer'


def run():
    header_art = "\n\t██╗    ██╗ ██████╗ ██╗    ██╗███████╗███████╗██████╗\n"
    header_art += "\t██║    ██║██╔═══██╗██║    ██║╚══███╔╝██╔════╝██╔══██╗\n"
    header_art += "\t██║ █╗ ██║██║   ██║██║ █╗ ██║  ███╔╝ █████╗  ██████╔╝\n"
    header_art += "\t██║███╗██║██║   ██║██║███╗██║ ███╔╝  ██╔══╝  ██╔══██╗\n"
    header_art += "\t╚███╔███╔╝╚██████╔╝╚███╔███╔╝███████╗███████╗██║  ██║\n"
    header_art += "\t╚══╝╚══╝  ╚═════╝  ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝\n"
    header = "\n******************************************************************************************\n"
    header += "* " + APP_NAME + " version " + APP_VERSION + " <" + WEBSITE_LINK + ">.\n"
    header += "* Copyright (C) " + COPYRIGHT_YEAR + " " + AUTHOR + "\n"
    header += "*\n"
    header += "* " + APP_NAME + " is free software: you can redistribute it and/or modify it under the terms of the\n"
    header += "* GNU General Public License as published by the Free Software Foundation, either version 3\n"
    header += "* of the License, or (at your option) any later version.\n"
    header += "*\n"
    header += "* " + APP_NAME + " is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without\n"
    header += "* even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the\n"
    header += "* GNU General Public License for more details.\n"
    header += "*\n"
    header += "* You should have received a copy of the GNU General Public License along with Foobar.\n"
    header += "* If not, see <https://www.gnu.org/licenses/>.\n"
    header += "******************************************************************************************\n"
    print(header_art, header)
    main.run()


if __name__ == "__main__":
    run()
