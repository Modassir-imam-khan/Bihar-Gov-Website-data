from selenium import webdriver
from helium import *
import pandas as pd
from pathlib import Path
import os
import numpy as np
import pdb
import openpyxl

post = ["Zila_parishad_member","Panchayat_samiti_member","Mukhiya","Sarpanch","ward_member","panch"]
district = ["PASCHIM_CHAMPARAN","PURVI_CHAMPARAN","SHEOHAR","SITAMARHI","MADHUBANI","SUPAUL","ARARIA","KISHANGANJ","PURNIA","KATIHAR",
            "MADHEPURA","SAHARSA","DARBHANGA","MUZAFFARPUR","GOPALGANJ","SIWAN","SARAN","VAISHALI","SAMASTIPUR","BEGUSARAI",
           "KHAGARIA","BHAGALPUR","BANKA","MUNGER","LAKHISARAI","SHEIKHPURA","NALANDA","PATNA","BHOJPUR","BUXAR","KAIMUR_BHABUA",
           "ROHTAS","ARWAL","JAHANABAD","AURANGABAD","GAYA","NAWADA","JAMUI"]
block = ["Terhagachh","Dighalbank","Bahadurganj","Thakurganj","Pothia","Kochadhaman","KISHANGANJ"]
panchayat = ["HALAMALA","BELWA","MOTIHARA_TALUKA","SIGHIA_KULAMANI","GACHHPARA","TEUSA","CHAKLA","MAHINGAON","DAULA","PICHHALA"]


# for Zila_parishad_member

brouser = start_chrome('http://sec.bihar.gov.in/wcl.aspx')
post_menu = brouser.find_element_by_xpath('//*[@id="ddlPostName"]').click()
post_option = brouser.find_element_by_xpath('//*[@id="ddlPostName"]/option[2]')
post_option.click()
wait_until(Text('District :').exists)
district_menu = brouser.find_element_by_xpath('//*[@id="ddlDistrict"]').click()
district_option = brouser.find_element_by_xpath('//*[@id="ddlDistrict"]/option[9]')
district_option.click()
click('view')
dfs = pd.read_html(brouser.page_source)
info_1 = dfs[1].to_dict()
info = dfs[1]
info['Post'] = 'Zila_parishad_member'
info['District'] = 'KISHANGANJ'
info['Block'] =  'N/A'
info['Panchayat'] = 'N/A'
info.to_excel('sheet-'+f"{post[0]}-{district[7]}.xlsx",index = False)
kill_browser()



#for "Panchayat_samiti_member","Mukhiya","Sarpanch"

brouser = start_chrome('http://sec.bihar.gov.in/wcl.aspx')
for i in range(3, 6):
    post_menu = brouser.find_element_by_xpath('//*[@id="ddlPostName"]').click()
    post_option = brouser.find_element_by_xpath('//*[@id="ddlPostName"]/option[{}]'.format(i))
    post_option.click()
    wait_until(Text('District :').exists)
    district_menu = brouser.find_element_by_xpath('//*[@id="ddlDistrict"]').click()
    district_option = brouser.find_element_by_xpath('//*[@id="ddlDistrict"]/option[9]')
    district_option.click()
    wait_until(Text('Block :').exists)
    block_menu = brouser.find_element_by_xpath('//*[@id="ddlBlok"]').click()
    print(i)
    for j in range(2,9): 
        block_option = brouser.find_element_by_xpath('//*[@id="ddlBlok"]/option[{}]'.format(j))
        block_option.click()
        click('view')
        df = pd.read_html(brouser.page_source)
        info = df[1]
        info['Post'] = post[i-2]
        info['District'] = 'KISHANGANJ'
        print(j)
        info['Block'] =  block[j-2]
        print(block[j-2])
        info['Panchayat'] = 'N/A'
        info.to_excel('sheet-'+f"{post[i-2]}-{district[7]}-{block[j-2]}.xlsx", index=False)    

kill_browser()

#for "ward_member","panch"
brouser = start_chrome('http://sec.bihar.gov.in/wcl.aspx')
for i in range(6, 8):
    post_menu = brouser.find_element_by_xpath('//*[@id="ddlPostName"]').click()
    post_option = brouser.find_element_by_xpath('//*[@id="ddlPostName"]/option[{}]'.format(i))
    post_option.click()
    wait_until(Text('District :').exists)
    district_menu = brouser.find_element_by_xpath('//*[@id="ddlDistrict"]').click()
    district_option = brouser.find_element_by_xpath('//*[@id="ddlDistrict"]/option[9]')
    district_option.click()
    wait_until(Text('Block :').exists)
    block_menu = brouser.find_element_by_xpath('//*[@id="ddlBlok"]').click()
    for k in range(2,9):
        block_option = brouser.find_element_by_xpath('//*[@id="ddlBlok"]/option[{}]'.format(k))
        block_option.click()
        wait_until(Text('Panchayat :').exists)
        for j in range(2, 12):
            panchayat_option = brouser.find_element_by_xpath('//*[@id="ddlPanchayat"]/option[{}]'.format(j))
            panchayat_option.click()
            click('view')
            df = pd.read_html(brouser.page_source)
            info = df[1]
            info['Post'] = post[i-2]
            info['District'] = 'KISHANGANJ'
            print(j)
            info['Block'] =  block[k-2]
            print(block[k-2])
            info['Panchayat'] = panchayat[j-2]
            print(panchayat[j-2])
            print(post[i-2])
            info.to_excel('sheet-'+f"{post[i-2]}-{district[7]}-{block[k-2]}-{panchayat[j-2]}.xlsx", index = False)

        
kill_browser()