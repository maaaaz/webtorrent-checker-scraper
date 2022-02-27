#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file is part of webtorrent_checker_scraper.
#
# Copyright (C) 2022, Thomas Debize <tdebize at mail.com>
# All rights reserved.
#
# webtorrent_checker_scraper is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# webtorrent_checker_scraper is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with webtorrent_checker_scraper.  If not, see <http://www.gnu.org/licenses/>.

from lxml.html.soupparser import fromstring

import argparse
import requests
import urllib
import json
import torf
import colorama
import termcolor

# Script version
VERSION = '1.0'

# Options definition
parser = argparse.ArgumentParser(description="version: " + VERSION)

input_grp = parser.add_argument_group('Input parameters')
input_grp.add_argument('-i', '--input-file', help='Input file containing a magnet link per line', default = None)
input_grp.add_argument('-t', '--autoadd-trackers', help='Automatically add popular trackers', action = 'store_true', default = False)

colorama.init()

def pretty_results(number):
    result = number
    if number >= 1:
        result = termcolor.colored(number, 'green', attrs=['bold'])
    
    return result

def analyze_result(result, line_magnet, line_unquoted_back):
    if 'seeds' in result.keys() and 'peers' in result.keys():
        seeds = result['seeds']
        peers = result['peers']
        print(f'DN:   "{line_magnet.dn}"')
        print(f'Hash: "{line_magnet.infohash.upper()}"')
        print('Seeds: %s' % pretty_results(seeds))
        print('Peers: %s' % pretty_results(peers))
        print(line_unquoted_back)
        print("\n----------------------------------\n")
    
    return None

def call_webtorrent(line_unquoted):
    base_url = 'https://checker.openwebtorrent.com/check?magnet='
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
    
    line_magnet = torf.Magnet.from_string(line_unquoted)
    line_quoted_plus = urllib.parse.quote_plus(line_unquoted)
    line_unquoted_back = urllib.parse.unquote(line_quoted_plus)
    
    url = base_url + line_quoted_plus
    result = json.loads(requests.get(url, headers=headers).content)
    
    analyze_result(result, line_magnet, line_unquoted_back)
    
    return None

def scrape(opts):
    with open(opts.input_file, mode='r', encoding="utf-8") as fd_input:
        for line in fd_input:
            line = line.strip()
            if line:
                line_unquoted = urllib.parse.unquote_plus(line)
                call_webtorrent(line_unquoted)
                
                if opts.autoadd_trackers:
                    auto_trackers = ['udp://tracker.opentrackr.org:1337/announce',
                                     'udp://open.tracker.cl:1337/announce',
                                     'udp://9.rarbg.com:2810/announce',
                                     'udp://exodus.desync.com:6969/announce',
                                     'udp://www.torrent.eu.org:451/announce',
                                     'udp://tracker1.bt.moack.co.kr:80/announce',
                                     'udp://tracker.zerobytes.xyz:1337/announce',
                                     'udp://tracker.torrent.eu.org:451/announce',
                                     'udp://tracker.tiny-vps.com:6969/announce',
                                     'udp://tracker.theoks.net:6969/announce',
                                     'udp://tracker.srv00.com:6969/announce',
                                     'udp://tracker.pomf.se:80/announce',
                                     'udp://tracker.openbittorrent.com:6969/announce',
                                     'udp://tracker.monitorit4.me:6969/announce',
                                     'udp://tracker.moeking.me:6969/announce',
                                     'udp://tracker.lelux.fi:6969/announce',
                                     'udp://tracker.jordan.im:6969/announce',
                                     'udp://tracker.dler.org:6969/announce',
                                     'udp://tracker.bitsearch.to:1337/announce',
                                     'udp://tracker.auctor.tv:6969/announce']
                    line_autoadded = line_unquoted + "".join("&tr=%s" % tracker for tracker in auto_trackers)
                    call_webtorrent(line_autoadded)
    
    return None

def main():
    """
        Dat main
    """
    options = parser.parse_args()
    results = scrape(options)
    
    return None

if __name__ == "__main__" :
    main()