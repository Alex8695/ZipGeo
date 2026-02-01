#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 13:42:44 2026

@author: alex
"""

class ZipGeo:
    
    def __importData(self):
        dataLines:list

        with open("src/data/zipGeoData.txt") as file:
            dataLines = file.readlines()
            
        self._dataMaster.clear()

        for line in dataLines[1:]:
            temp = line.split("|")
            self._dataMaster[temp[0]] = [float(temp[6].strip()),float(temp[7].strip())]
        
        pass

    def __init__(self):
        self._dataMaster = {}
        self.__importData()
        pass


    def Find(self, zipcode:str):
        """
        Find lattitude and longitude by ZIP code\n
        ZipGeo.Find("48823")

        Parameters
        ----------
        zipcode : str
            ZIP Code being searched.

        Returns
        -------
        dict
            zip, lat, lon.

        """

        q = self._dataMaster[zipcode]
        return {"zip":zipcode,"lat":self._dataMaster[zipcode][0],"lon":self._dataMaster[zipcode][1]}
    
    
if __name__ == "__main__":
    zg = ZipGeo()
    print(zg.Find("48823"))
