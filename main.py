#!/usr/bin/env python3

import os
import sys
import getpass
import json

from colorama import Fore, init
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

from core.scanner import PhoneScanner
from core.social_mapper import SocialMapper
from core.image_scraper import ImageScraper
from core.geolocate import CellGeoTracker
from core.report_gen import ReportGenerator

init(autoreset=True)

# Login credentials
USERNAME = "python3"
PASSWORD = "jr11"


def login():
    print(Fore.CYAN + "\n===== PhantomTrace Login =====")

    username = input("Enter ID: ")
    password = getpass.getpass("Enter Password: ")

    if username == USERNAME and password == PASSWORD:
        print(Fore.GREEN + "[+] Login successful!")
        return True

    print(Fore.RED + "[-] Invalid ID or password.")
    return False


class PhantomTrace:

    def __init__(self, number: str):
        self.number = number

        self.data = {
            "phone": number,
            "valid": False,
            "carrier": None,
            "region": None,
            "timezone": None,
            "name": None,
            "social_profiles": [],
            "images": [],
            "last_location": None,
            "accuracy_radius": None,
            "timestamp": None,
            "call_pattern": None,
        }

    def run(self):
        print(Fore.CYAN + "[*] Initiating PhantomTrace scan...")

        scanner = PhoneScanner(self.number)

        if not scanner.validate():
            print(Fore.RED + "[-] Invalid phone number.")
            return

        self.data.update(scanner.scan())

        print(
            Fore.GREEN
            + f"[+] Number validated: "
            f"{self.data.get('region', 'Unknown')} | "
            f"{self.data.get('carrier', 'Unknown')}"
        )

        try:
            mapper = SocialMapper(self.number)
            profiles = mapper.search() or []

            self.data["social_profiles"] = profiles

            print(
                Fore.YELLOW
                + f"[~] Found {len(profiles)} social profiles"
            )

            scraper = ImageScraper(profiles)
            images = scraper.harvest() or []

            self.data["images"] = images

            print(
                Fore.YELLOW
                + f"[~] Collected {len(images)} image results"
            )

        except Exception as error:
            print(Fore.RED + f"[-] Public-source lookup failed: {error}")

        # A phone number alone cannot reliably reveal live GPS location.
        self.data["last_location"] = None

        try:
            os.makedirs("output", exist_ok=True)
            ReportGenerator(self.data).generate()

            print(
                Fore.GREEN
                + "[+] Report saved: output/report.html"
            )

        except Exception as error:
            print(Fore.RED + f"[-] Report generation failed: {error}")


if __name__ == "__main__":

    if not login():
        sys.exit(1)

    if len(sys.argv) != 2:
        print(
            f"Usage: {sys.argv[0]} "
            "<full_phone_number_with_country_code>"
        )
        print(f"Example: {sys.argv[0]} +919876543210")
        sys.exit(1)

    tool = PhantomTrace(sys.argv[1])
    tool.run()