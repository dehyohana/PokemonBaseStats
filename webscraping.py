from bs4 import BeautifulSoup as bs
import pandas as pd
import requests


class Scrapper:
    def __init__(self) -> None:
        self.url = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_base_stats_(Generation_VIII-present)"

    def _get_id(self, soup: bs) -> list:
        """Return id list

        Args:
            soup (bs): BeautifulSoup

        Returns:
            list: id_list[int]
        """
        list_id = soup.find_all("td", class_="r")
        for i in range(len(list_id)):
            list_id[i] = int(list_id[i].text.rstrip("\n"))
        return list_id

    def _get_pokemon(self, soup: bs) -> list:
        """Return list_pokemon

        Args:
            soup (bs): BeautifulSoup

        Returns:
            list: list_pokemon[string]
        """
        list_pokemon = soup.find_all("td", class_="l")
        for i in range(len(list_pokemon)):
            list_pokemon[i] = list_pokemon[i].text.rstrip("\n")
        return list_pokemon

    def _get_hp(self, soup: bs) -> list:
        """Return hp list

        Args:
            soup (bs): BeautifulSoup

        Returns:
            list: list_hp[int]
        """
        list_hp = soup.find_all("td", style="background:#FF5959")
        for i in range(len(list_hp)):
            list_hp[i] = int(list_hp[i].text.rstrip("\n"))
        return list_hp

    def _get_attack(self, soup: bs) -> list:
        """Return attack list

        Args:
            soup (bs): BeautifulSoup

        Returns:
            list: list_attack[int]
        """
        list_attack = soup.find_all("td", style="background:#F5AC78")
        for i in range(len(list_attack)):
            list_attack[i] = int(list_attack[i].text.rstrip("\n"))
        return list_attack

    def _get_defense(self, soup: bs) -> list:
        """Return defense list

        Args:
            soup (bs): BeautifulSoup

        Returns:
            list: list_defense[int]
        """
        list_defense = soup.find_all("td", style="background:#FAE078")
        for i in range(len(list_defense)):
            list_defense[i] = int(list_defense[i].text.rstrip("\n"))
        return list_defense

    def _get_sp_attack(self, soup: bs) -> list:
        """Return special attack list

        Args:
            soup (bs): BeautifulSoup

        Returns:
            list: list_sp_attack[int]
        """
        list_sp_attack = soup.find_all("td", style="background:#9DB7F5")
        for i in range(len(list_sp_attack)):
            list_sp_attack[i] = int(list_sp_attack[i].text.rstrip("\n"))
        return list_sp_attack

    def _get_sp_defense(self, soup: bs) -> list:
        """Return special defense list

        Args:
            soup (bs): BeautifulSoup

        Returns:
            list: list_sp_defense[int]
        """
        list_sp_defense = soup.find_all("td", style="background:#A7DB8D")
        for i in range(len(list_sp_defense)):
            list_sp_defense[i] = int(list_sp_defense[i].text.rstrip("\n"))
        return list_sp_defense

    def _get_speed(self, soup: bs) -> list:
        """Return speed list

        Args:
            soup (bs): BeautifulSoup

        Returns:
            list: speed_list[int]
        """
        list_speed = soup.find_all("td", style="background:#FA92B2")
        for i in range(len(list_speed)):
            list_speed[i] = int(list_speed[i].text.rstrip("\n"))
        return list_speed

    def _get_total(self, soup: bs) -> list:
        """Return status sum

        Args:
            soup (bs): BeautifulSoup

        Returns:
            list: list_total[int]
        """
        list_hp = self._get_hp(soup)
        list_attack = self._get_attack(soup)
        list_defense = self._get_defense(soup)
        list_sp_att = self._get_sp_attack(soup)
        list_sp_def = self._get_defense(soup)
        list_speed = self._get_speed(soup)
        total = [None] * len(list_hp)

        for i in range(len(list_hp)):
            total[i] = (
                list_hp[i]
                + list_attack[i]
                + list_defense[i]
                + list_sp_att[i]
                + list_sp_def[i]
                + list_speed[i]
            )
        return total

    def _get_average(self, soup: bs) -> list:
        """Return average status

        Args:
            soup (bs): BeautifulSoup

        Returns:
            list: list_average[float]
        """
        list_total = self._get_total(soup)
        list_average = [None] * len(list_total)
        for i in range(len(list_total)):
            list_average[i] = round(float(list_total[i]) / 6, 2)
        return list_average

    def _build_json(self, soup: bs) -> pd.DataFrame:
        """built dataframe of pokemon's stats ['id','pokemon','hp','att','def','sp_att','sp_def','speed','total','average']

        Args:
            soup (bs): BeautifulSoup

        Returns:
            pd.DataFrame: df_pokemon_stats
        """
        df = pd.DataFrame(
            columns=[
                "id",
                "pokemon",
                "hp",
                "attack",
                "defense",
                "sp_attack",
                "sp_defense",
                "speed",
                "total",
                "average",
            ]
        )

        list_id = self._get_id(soup)
        list_pokemon = self._get_pokemon(soup)
        list_hp = self._get_hp(soup)
        list_attack = self._get_attack(soup)
        list_defense = self._get_defense(soup)
        list_sp_att = self._get_sp_attack(soup)
        list_sp_def = self._get_defense(soup)
        list_speed = self._get_speed(soup)
        list_total = self._get_total(soup)
        list_average = self._get_average(soup)

        for i in range(len(list_id)):
            df2 = pd.DataFrame(
                {
                    "id": [list_id[i]],
                    "pokemon": [list_pokemon[i]],
                    "hp": [list_hp[i]],
                    "attack": [list_attack[i]],
                    "defense": [list_defense[i]],
                    "sp_attack": [list_sp_att[i]],
                    "sp_defense": [list_sp_def[i]],
                    "sp_defense": [list_defense[i]],
                    "speed": [list_speed[i]],
                    "total": [list_total[i]],
                    "average": [list_average[i]],
                }
            )
            df = pd.concat([df, df2], ignore_index=True)
        return df

    def scrapping_pokemon(self) -> pd.DataFrame:
        """Return dataframe to be consumed in main program

        Returns:
            pd.DataFrame: dataframe with pokemon stats
        """
        r = requests.get(self.url)
        soup = bs(r.text, "lxml")
        return self._build_json(soup)
