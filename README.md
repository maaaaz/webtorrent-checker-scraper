webtorrent_checker_scraper
==========================

Description
-----------
A simple script to scrape results of [WebTorrent Checker](https://checker.openwebtorrent.com).


Usage
-----
Put your magnet links in a text file, one entry per line (empty lines are ignored) and pass it with the `-i` option.  

### Options
```
$ python3 webtorrent_checker_scraper.py -i links.txt
usage: webtorrent_checker_scraper.py [-h] [-i INPUT_FILE] [-t]

version: 1.0

optional arguments:
  -h, --help            show this help message and exit

Input parameters:
  -i INPUT_FILE, --input-file INPUT_FILE
                        Input file containing a magnet link per line
  -t, --autoadd-trackers
                        Automatically add popular trackers
```

### Examples
```
$ cat links.txt
magnet:?xt=urn:btih:ada00c203f72ddf9603e49ad1c996f83cf6695db&dn=kali-linux-2022.1-installer-everything-amd64.iso&tr=udp://tracker.openbittorrent.com:80&tr=udp://tracker.opentrackr.org:1337/announce
magnet:?xt=urn:btih:28c55196f57753c40aceb6fb58617e6995a7eddb&dn=debian-11.2.0-amd64-netinst.iso&tr=udp://tracker.openbittorrent.com:80&tr=udp://tracker.opentrackr.org:1337/announce

$ python3 webtorrent_checker_scraper.py -i links.txt
DN:   "kali-linux-2022.1-installer-everything-amd64.iso"
Hash: "ADA00C203F72DDF9603E49AD1C996F83CF6695DB"
Seeds: 4
Peers: 3
magnet:?xt=urn:btih:ada00c203f72ddf9603e49ad1c996f83cf6695db&dn=kali-linux-2022.1-installer-everything-amd64.iso&tr=udp://tracker.openbittorrent.com:80&tr=udp://tracker.opentrackr.org:1337/announce

----------------------------------

DN:   "debian-11.2.0-amd64-netinst.iso"
Hash: "28C55196F57753C40ACEB6FB58617E6995A7EDDB"
Seeds: 7
Peers: 0
magnet:?xt=urn:btih:28c55196f57753c40aceb6fb58617e6995a7eddb&dn=debian-11.2.0-amd64-netinst.iso&tr=udp://tracker.openbittorrent.com:80&tr=udp://tracker.opentrackr.org:1337/announce

----------------------------------
```
  

Changelog
---------
* version 1.0 - 02/27/2022: Initial commit

Copyright and license
---------------------
webtorrent_checker_scraper is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

webtorrent_checker_scraper is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with webtorrent_checker_scraper. 
If not, see http://www.gnu.org/licenses/.

Contact
-------
* Thomas Debize < tdebize at mail d0t com >