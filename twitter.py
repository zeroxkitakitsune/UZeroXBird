import sys, json, argparse
import os
import requests
import json
import time
import random
import uncurl
import re

class Twitter:

    def __init__(self):
        self.listAccounts = []

    def link_account(self, name, curl, proxy):

        curl_list = curl.split('\n')
        final_curl_list = []
        
        for string in curl_list:
            new_string = ''
            index = 0
            for index in range(len(string)):
                if index != len(string) - 1:
                    if string != curl_list[len(final_curl_list) - 1]:
                        new_string += string[index]
                    else:
                        new_string += string
            final_curl_list.append(new_string)

        curl_str = ''
        for ele in final_curl_list:
            curl_str += ele 
        
        context = uncurl.parse_context(curl_str)
        
        print(context.url)
        reqUrl = context.url

        payload = context.data
        account = {}
        account['name'] = name
        account['guest_id'] = context.cookies['guest_id']
        account['headers'] = context.headers
        account['headers']['referer'] = 'https://twitter.com/home'
        account['cookies'] = context.cookies
        account['proxies'] = {
            'http':proxy,
            'https': proxy
        }

        self.listAccounts.append(account)

    def export_sessions(self):
        ofile = open('sessions.json', 'w')
        sessions = json.dumps(self.listAccounts)
        ofile.write(sessions)
        print("Updated sessions.json")
    
    def import_sessions(self, fileName):
        
        with open(fileName, 'r') as j:
            sessions = json.loads(j.read())

        for session in sessions:
            self.listAccounts.append({'name': session['name'], 'guest_id': session['guest_id'], 'headers': session['headers'], 'cookies': session['cookies'], 'proxies':session['proxies']})
    
    def follow(self, names, username):

        accounts_to_use = []
        for name in names:
            for account in self.listAccounts:
                if account['name'] == name:
                   accounts_to_use.append(account) 
                  
        for account in accounts_to_use:
            # Making the request

            params = {
                'variables': '{"screen_name":"' + username + '","withSafetyModeUserFields":true}',
                'features': '{"blue_business_profile_image_shape_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true}',
            }

            response = requests.request('GET', 'https://twitter.com/i/api/graphql/sLVLhk0bGj3MVFEKTdax1w/UserByScreenName', params=params, cookies=account['cookies'], headers=account['headers'], proxies=account['proxies'])

            if response.status_code != 200:
                return "Request returned an error: {} {}".format(response.status_code, response.text)

            data = json.loads(response.text) 

            user_id = data['data']['user']['result']['rest_id']
        
            data = {
                'include_profile_interstitial_type': '1',
                'include_blocking': '1',
                'include_blocked_by': '1',
                'include_followed_by': '1',
                'include_want_retweets': '1',
                'include_mute_edge': '1',
                'include_can_dm': '1',
                'include_can_media_tag': '1',
                'include_ext_has_nft_avatar': '1',
                'include_ext_is_blue_verified': '1',
                'include_ext_verified_type': '1',
                'include_ext_profile_image_shape': '1',
                'skip_status': '1',
                'user_id': f'{user_id}',
            }
            
            account['headers']['referer'] = f'https://twitter.com/{username}'
            account['headers']['content-type'] = 'application/x-www-form-urlencoded'
            response = requests.post('https://twitter.com/i/api/1.1/friendships/create.json', headers=account['headers'], cookies=account['cookies'],data=data, proxies=account['proxies'])
            
            if response.status_code != 200:
                return "Request returned an error: {} {}".format(response.status_code, response.text)
        
        return "Success"

    def tweet(self, names, text):
    
        payload = {
            'variables': {
                'tweet_text': text,
                'dark_request': False,
                'media': {
                    'media_entities': [],
                    'possibly_sensitive': False,
                },
                'withDownvotePerspective': False,
                'semantic_annotation_ids': [],
            },
            'features': {
                'tweetypie_unmention_optimization_enabled': True,
                'vibe_api_enabled': True,
                'responsive_web_edit_tweet_api_enabled': True,
                'graphql_is_translatable_rweb_tweet_is_translatable_enabled': True,
                'view_counts_everywhere_api_enabled': True,
                'longform_notetweets_consumption_enabled': True,
                'tweet_awards_web_tipping_enabled': False,
                'interactive_text_enabled': True,
                'responsive_web_text_conversations_enabled': False,
                'longform_notetweets_rich_text_read_enabled': True,
                'blue_business_profile_image_shape_enabled': True,
                'responsive_web_graphql_exclude_directive_enabled': True,
                'verified_phone_label_enabled': False,
                'freedom_of_speech_not_reach_fetch_enabled': False,
                'standardized_nudges_misinfo': True,
                'tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled': False,
                'responsive_web_graphql_timeline_navigation_enabled': True,
                'responsive_web_graphql_skip_user_profile_image_extensions_enabled': False,
                'responsive_web_enhance_cards_enabled': False,
            },
            'queryId': 'shjyg0Y1ez2QoihsYD05xA',
        }
        
        accounts_to_use = []
        for name in names:
            for account in self.listAccounts:
                if account['name'] == name:
                   accounts_to_use.append(account) 

        for account in accounts_to_use:
            account['headers']['referer'] = 'https://twitter.com/compose/tweet'
            account['headers']['content-type'] = 'application/json'       
            response = requests.request('POST', 'https://twitter.com/i/api/graphql/shjyg0Y1ez2QoihsYD05xA/CreateTweet', json=payload, headers=account['headers'], cookies=account['cookies'], proxies=account['proxies'])
            if response.status_code != 200:

                print("Request returned an error: {} {}".format(response.status_code, response.text))
                return "Request returned an error: {} {}".format(response.status_code, response.text)
        return "Success"

    
    def retweet(self, names, link, pause):

        tweetid = link.rsplit("/")
        
        #print("Tweet ID: " + link[len(link) - 1]) 
        payload = {"variables":{"tweet_id":f"{tweetid[len(tweetid) - 1]}","dark_request":False},"queryId":"ojPdsZsimiJrUGLR1sjUtA"}

        accounts_to_use = []
        for name in names:
            for account in self.listAccounts:
                if account['name'] == name:
                   accounts_to_use.append(account) 
        
        for account in accounts_to_use:
            account['headers']['referer'] = f'{link}'
            account['headers']['content-type'] = 'application/json'     
            response = requests.request('POST', 'https://twitter.com/i/api/graphql/ojPdsZsimiJrUGLR1sjUtA/CreateRetweet', json=payload, headers=account['headers'], cookies=account['cookies'], proxies=account['proxies'])
            if response.status_code != 200:
                return "Request returned an error: {} {}".format(response.status_code, response.text)
            if pause:
                time.sleep(random.randint(1, 60))
            else:
                time.sleep(5)
        return "Success"

    def like(self, names, link):

        link = link.rsplit("/")
        
        #print("Tweet ID: " + link[len(link) - 1]) 
        json_data = {
            'variables': {
                'tweet_id': f'{str(link[len(link) - 1])}',
            },
            'queryId': 'lI07N6Otwv1PhnEgXILM7A',
        }

        accounts_to_use = []
        for name in names:
            for account in self.listAccounts:
                if account['name'] == name:
                   accounts_to_use.append(account) 
        

        for account in accounts_to_use:
            account['headers']['referer'] = f'{link}'
            account['headers']['content-type'] = 'application/json'   
            response = requests.request('POST', 'https://twitter.com/i/api/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet', json=json_data, headers=account['headers'], cookies=account['cookies'],proxies=account['proxies'])

            if response.status_code != 200:
                return "Request returned an error: {} {}".format(response.status_code, response.text)
        return "Success"
    
    def delete(self, names):
        for name in names:
            for account in self.listAccounts:
                if account['name'] == name:
                   self.listAccounts.remove(account)