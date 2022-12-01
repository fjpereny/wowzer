
import main


APP_NAME = 'wowzer'
APP_VERSION = '0.0.1'
AUTHOR = 'Frank Pereny'
COPRIGHT_YEAR = '2022'
WEBSITE_LINK = 'https://github.com/fjpereny/wowzer'

if __name__ == "__main__":

    header_art = "\n██╗    ██╗ ██████╗ ██╗    ██╗███████╗███████╗██████╗\n"
    header_art += "██║    ██║██╔═══██╗██║    ██║╚══███╔╝██╔════╝██╔══██╗\n"
    header_art += "██║ █╗ ██║██║   ██║██║ █╗ ██║  ███╔╝ █████╗  ██████╔╝\n"
    header_art += "██║███╗██║██║   ██║██║███╗██║ ███╔╝  ██╔══╝  ██╔══██╗\n"
    header_art += "╚███╔███╔╝╚██████╔╝╚███╔███╔╝███████╗███████╗██║  ██║\n"
    header_art += "╚══╝╚══╝  ╚═════╝  ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝\n"
    header = "\n******************************************************************************************\n"
    header += "* " + APP_NAME + " version " + APP_VERSION + " <" + WEBSITE_LINK + ">.\n"
    header += "* Copyright (C) " + COPRIGHT_YEAR + " " + AUTHOR + "\n"
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
