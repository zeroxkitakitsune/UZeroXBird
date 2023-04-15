import requests
import json
import uncurl

# print(uncurl.parse("curl 'https://twitter.com/i/api/graphql/shjyg0Y1ez2QoihsYD05xA/CreateTweet' \
#   -H 'authority: twitter.com' \
#   -H 'accept: */*' \
#   -H 'accept-language: en-GB,en;q=0.7' \
#   -H 'authorization: Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA' \
#   -H 'content-type: application/json' \
#   -H 'cookie: kdt=Cndw5P0oJTKw9qDmfk5kuufcc7sw7ECciPauh4jH; dnt=1; d_prefs=MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; guest_id_ads=v1%3A168082909397916576; guest_id_marketing=v1%3A168082909397916576; _ga=GA1.2.381762403.1680472963; ads_prefs=\"HBISAAA=\"; auth_multi=\"1642366875312029697:ae2b8d65e8e3fe0137cd72b658641ecb5de0a78d\"; auth_token=2b5cdfe064d280cab51ee91a4c0bbfad8608bb38; personalization_id=\"v1_qotda8uUh5NU6A+AIIYtBg==\"; guest_id=v1%3A168109680560691920; twid=u%3D1623424053649240065; ct0=dfbcdbb17c5df03a5228368032e240b124d734ae870a766cd1c9f6b420c516829096acb610bd8e6debfb9992ffd1eab061ad1bfdc7100ee7b25e23dee64e2edc4faa9acdc5a76d4772402d878dedeef8; des_opt_in=Y; external_referer=padhuUp37zgjsdHoV5WIY%2B0RxDIrwK%2FmBHQ7dfvVwvc%3D|0|8e8t2xd8A2w%3D; mbox=PC#8b63e013864742fbab4cc9efb3d61389.34_0#1744411331|session#bc29c9458531475eab9d1ae5f9a98ca0#1681168391; lang=en' \
#   -H 'origin: https://twitter.com' \
#   -H 'referer: https://twitter.com/compose/tweet' \
#   -H 'sec-ch-ua: \"Chromium\";v=\"112\", \"Brave\";v=\"112\", \"Not:A-Brand\";v=\"99\"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: \"Linux\"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'sec-gpc: 1' \
#   -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36' \
#   -H 'x-csrf-token: dfbcdbb17c5df03a5228368032e240b124d734ae870a766cd1c9f6b420c516829096acb610bd8e6debfb9992ffd1eab061ad1bfdc7100ee7b25e23dee64e2edc4faa9acdc5a76d4772402d878dedeef8' \
#   -H 'x-twitter-active-user: yes' \
#   -H 'x-twitter-auth-type: OAuth2Session' \
#   -H 'x-twitter-client-language: en' \
#   --data-raw '{\"variables\":{\"tweet_text\":\"@Ubisoft asdasd\",\"dark_request\":false,\"media\":{\"media_entities\":[],\"possibly_sensitive\":false},\"withDownvotePerspective\":false,\"semantic_annotation_ids\":[]},\"features\":{\"tweetypie_unmention_optimization_enabled\":true,\"vibe_api_enabled\":true,\"responsive_web_edit_tweet_api_enabled\":true,\"graphql_is_translatable_rweb_tweet_is_translatable_enabled\":true,\"view_counts_everywhere_api_enabled\":true,\"longform_notetweets_consumption_enabled\":true,\"tweet_awards_web_tipping_enabled\":false,\"interactive_text_enabled\":true,\"responsive_web_text_conversations_enabled\":false,\"longform_notetweets_rich_text_read_enabled\":false,\"blue_business_profile_image_shape_enabled\":false,\"responsive_web_graphql_exclude_directive_enabled\":true,\"verified_phone_label_enabled\":false,\"freedom_of_speech_not_reach_fetch_enabled\":false,\"standardized_nudges_misinfo\":true,\"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled\":false,\"responsive_web_graphql_timeline_navigation_enabled\":true,\"responsive_web_graphql_skip_user_profile_image_extensions_enabled\":false,\"responsive_web_enhance_cards_enabled\":false},\"queryId\":\"shjyg0Y1ez2QoihsYD05xA\"}' \
#   --compressed"))

context = uncurl.parse_context("curl 'https://twitter.com/i/api/graphql/shjyg0Y1ez2QoihsYD05xA/CreateTweet' \
  -H 'authority: twitter.com' \
  -H 'accept: */*' \
  -H 'accept-language: en-GB,en;q=0.7' \
  -H 'authorization: Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA' \
  -H 'content-type: application/json' \
  -H 'cookie: kdt=Cndw5P0oJTKw9qDmfk5kuufcc7sw7ECciPauh4jH; dnt=1; d_prefs=MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; guest_id_ads=v1%3A168082909397916576; guest_id_marketing=v1%3A168082909397916576; _ga=GA1.2.381762403.1680472963; ads_prefs=\"HBISAAA=\"; auth_multi=\"1642366875312029697:ae2b8d65e8e3fe0137cd72b658641ecb5de0a78d\"; auth_token=2b5cdfe064d280cab51ee91a4c0bbfad8608bb38; personalization_id=\"v1_qotda8uUh5NU6A+AIIYtBg==\"; guest_id=v1%3A168109680560691920; twid=u%3D1623424053649240065; ct0=dfbcdbb17c5df03a5228368032e240b124d734ae870a766cd1c9f6b420c516829096acb610bd8e6debfb9992ffd1eab061ad1bfdc7100ee7b25e23dee64e2edc4faa9acdc5a76d4772402d878dedeef8; des_opt_in=Y; external_referer=padhuUp37zgjsdHoV5WIY%2B0RxDIrwK%2FmBHQ7dfvVwvc%3D|0|8e8t2xd8A2w%3D; mbox=PC#8b63e013864742fbab4cc9efb3d61389.34_0#1744411331|session#bc29c9458531475eab9d1ae5f9a98ca0#1681168391; lang=en' \
  -H 'origin: https://twitter.com' \
  -H 'referer: https://twitter.com/compose/tweet' \
  -H 'sec-ch-ua: \"Chromium\";v=\"112\", \"Brave\";v=\"112\", \"Not:A-Brand\";v=\"99\"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: \"Linux\"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-gpc: 1' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36' \
  -H 'x-csrf-token: dfbcdbb17c5df03a5228368032e240b124d734ae870a766cd1c9f6b420c516829096acb610bd8e6debfb9992ffd1eab061ad1bfdc7100ee7b25e23dee64e2edc4faa9acdc5a76d4772402d878dedeef8' \
  -H 'x-twitter-active-user: yes' \
  -H 'x-twitter-auth-type: OAuth2Session' \
  -H 'x-twitter-client-language: en' \
  --data-raw '{\"variables\":{\"tweet_text\":\"@Ubisoft asdasdasdasdasd\",\"dark_request\":false,\"media\":{\"media_entities\":[],\"possibly_sensitive\":false},\"withDownvotePerspective\":false,\"semantic_annotation_ids\":[]},\"features\":{\"tweetypie_unmention_optimization_enabled\":true,\"vibe_api_enabled\":true,\"responsive_web_edit_tweet_api_enabled\":true,\"graphql_is_translatable_rweb_tweet_is_translatable_enabled\":true,\"view_counts_everywhere_api_enabled\":true,\"longform_notetweets_consumption_enabled\":true,\"tweet_awards_web_tipping_enabled\":false,\"interactive_text_enabled\":true,\"responsive_web_text_conversations_enabled\":false,\"longform_notetweets_rich_text_read_enabled\":false,\"blue_business_profile_image_shape_enabled\":false,\"responsive_web_graphql_exclude_directive_enabled\":true,\"verified_phone_label_enabled\":false,\"freedom_of_speech_not_reach_fetch_enabled\":false,\"standardized_nudges_misinfo\":true,\"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled\":false,\"responsive_web_graphql_timeline_navigation_enabled\":true,\"responsive_web_graphql_skip_user_profile_image_extensions_enabled\":false,\"responsive_web_enhance_cards_enabled\":false},\"queryId\":\"shjyg0Y1ez2QoihsYD05xA\"}' \
  --compressed")

  curl 'https://twitter.com/i/api/graphql/shjyg0Y1ez2QoihsYD05xA/CreateTweet' \
  -H 'authority: twitter.com' \
  -H 'accept: */*' \
  -H 'accept-language: en-GB,en;q=0.5' \
  -H 'authorization: Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA' \
  -H 'content-type: application/json' \
  -H 'cookie: kdt=Cndw5P0oJTKw9qDmfk5kuufcc7sw7ECciPauh4jH; dnt=1; ads_prefs="HBISAAA="; auth_multi="1642366875312029697:ae2b8d65e8e3fe0137cd72b658641ecb5de0a78d"; auth_token=2b5cdfe064d280cab51ee91a4c0bbfad8608bb38; guest_id=v1%3A168109680560691920; twid=u%3D1623424053649240065; ct0=dfbcdbb17c5df03a5228368032e240b124d734ae870a766cd1c9f6b420c516829096acb610bd8e6debfb9992ffd1eab061ad1bfdc7100ee7b25e23dee64e2edc4faa9acdc5a76d4772402d878dedeef8; des_opt_in=Y; lang=en; d_prefs=MjoxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw' \
  -H 'origin: https://twitter.com' \
  -H 'referer: https://twitter.com/compose/tweet' \
  -H 'sec-ch-ua: "Chromium";v="112", "Brave";v="112", "Not:A-Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-gpc: 1' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36' \
  -H 'x-csrf-token: dfbcdbb17c5df03a5228368032e240b124d734ae870a766cd1c9f6b420c516829096acb610bd8e6debfb9992ffd1eab061ad1bfdc7100ee7b25e23dee64e2edc4faa9acdc5a76d4772402d878dedeef8' \
  -H 'x-twitter-active-user: yes' \
  -H 'x-twitter-auth-type: OAuth2Session' \
  -H 'x-twitter-client-language: en' \
  --data-raw '{"variables":{"tweet_text":"asddwwd","dark_request":false,"media":{"media_entities":[],"possibly_sensitive":false},"withDownvotePerspective":false,"semantic_annotation_ids":[]},"features":{"tweetypie_unmention_optimization_enabled":true,"vibe_api_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"tweet_awards_web_tipping_enabled":false,"interactive_text_enabled":true,"responsive_web_text_conversations_enabled":false,"longform_notetweets_rich_text_read_enabled":true,"blue_business_profile_image_shape_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":false,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"responsive_web_enhance_cards_enabled":false},"queryId":"shjyg0Y1ez2QoihsYD05xA"}' \
  --compressed

# context2 = uncurl.parse_context("curl 'https://twitter.com/i/api/graphql/ojPdsZsimiJrUGLR1sjUtA/CreateRetweet' \
#   -H 'authority: twitter.com' \
#   -H 'accept: */*' \
#   -H 'accept-language: en-GB,en;q=0.5' \
#   -H 'authorization: Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA' \
#   -H 'content-type: application/json' \
#   -H 'cookie: kdt=Cndw5P0oJTKw9qDmfk5kuufcc7sw7ECciPauh4jH; dnt=1; d_prefs=MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; guest_id_ads=v1%3A168082909397916576; guest_id_marketing=v1%3A168082909397916576; _ga=GA1.2.381762403.1680472963; ads_prefs="HBISAAA="; auth_multi="1642366875312029697:ae2b8d65e8e3fe0137cd72b658641ecb5de0a78d"; auth_token=2b5cdfe064d280cab51ee91a4c0bbfad8608bb38; personalization_id="v1_qotda8uUh5NU6A+AIIYtBg=="; guest_id=v1%3A168109680560691920; twid=u%3D1623424053649240065; ct0=dfbcdbb17c5df03a5228368032e240b124d734ae870a766cd1c9f6b420c516829096acb610bd8e6debfb9992ffd1eab061ad1bfdc7100ee7b25e23dee64e2edc4faa9acdc5a76d4772402d878dedeef8; des_opt_in=Y; external_referer=padhuUp37zgjsdHoV5WIY%2B0RxDIrwK%2FmBHQ7dfvVwvc%3D|0|8e8t2xd8A2w%3D; mbox=PC#8b63e013864742fbab4cc9efb3d61389.34_0#1744411331|session#bc29c9458531475eab9d1ae5f9a98ca0#1681168391; lang=en' \
#   -H 'origin: https://twitter.com' \
#   -H 'referer: https://twitter.com/soren_iverson' \
#   -H 'sec-ch-ua: "Chromium";v="112", "Brave";v="112", "Not:A-Brand";v="99"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "Linux"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'sec-gpc: 1' \
#   -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36' \
#   -H 'x-csrf-token: dfbcdbb17c5df03a5228368032e240b124d734ae870a766cd1c9f6b420c516829096acb610bd8e6debfb9992ffd1eab061ad1bfdc7100ee7b25e23dee64e2edc4faa9acdc5a76d4772402d878dedeef8' \
#   -H 'x-twitter-active-user: yes' \
#   -H 'x-twitter-auth-type: OAuth2Session' \
#   -H 'x-twitter-client-language: en' \
#   --data-raw '{"variables":{"tweet_id":"1646513580345536513","dark_request":false},"queryId":"ojPdsZsimiJrUGLR1sjUtA"}' \
#   --compressed")

reqUrl = context.url

headersList = context.headers
cookie = context.cookies

payload = context.data

response = requests.request("POST", reqUrl, data=payload,  headers=headersList, cookies=cookie)

print(response.text)

# reqUrl = \"https://twitter.com/i/api/graphql/ojPdsZsimiJrUGLR1sjUtA/CreateRetweet\"
 

# headersList = {
#  \"authority\": \"twitter.com\",
#  \"accept\": \"*/*\",
#  \"accept-language\": \"en-GB,en;q=0.7\",
#  \"authorization\": \"Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA\",
#  \"content-type\": \"application/json\",
#  \"cookie\": 'kdt=Cndw5P0oJTKw9qDmfk5kuufcc7sw7ECciPauh4jH; dnt=1; d_prefs=MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; guest_id_ads=v1%3A168082909397916576; guest_id_marketing=v1%3A168082909397916576; _ga=GA1.2.381762403.1680472963; ads_prefs=\"HBISAAA=\"; auth_multi=\"1642366875312029697:ae2b8d65e8e3fe0137cd72b658641ecb5de0a78d\"; auth_token=2b5cdfe064d280cab51ee91a4c0bbfad8608bb38; personalization_id=\"v1_qotda8uUh5NU6A+AIIYtBg==\"; guest_id=v1%3A168109680560691920; twid=u%3D1623424053649240065; ct0=dfbcdbb17c5df03a5228368032e240b124d734ae870a766cd1c9f6b420c516829096acb610bd8e6debfb9992ffd1eab061ad1bfdc7100ee7b25e23dee64e2edc4faa9acdc5a76d4772402d878dedeef8; des_opt_in=Y; external_referer=padhuUp37zgjsdHoV5WIY%2B0RxDIrwK%2FmBHQ7dfvVwvc%3D|0|8e8t2xd8A2w%3D; mbox=PC#8b63e013864742fbab4cc9efb3d61389.34_0#1744411331|session#bc29c9458531475eab9d1ae5f9a98ca0#1681168391; lang=en',
#  \"origin\": \"https://twitter.com\",
#  \"referer\": \"https://twitter.com/home\",
#  \"sec-ch-ua\": 'Chromium\";v=\"112\", \"Brave\";v=\"112\", \"Not:A-Brand\";v=\"99',
#  \"sec-ch-ua-mobile\": \"?0\",
#  \"sec-ch-ua-platform\": \"Linux\",
#  \"sec-fetch-dest\": \"empty\",
#  \"sec-fetch-mode\": \"cors\",
#  \"sec-fetch-site\": \"same-origin\",
#  \"sec-gpc\": \"1\",
#  \"user-agent\": \"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36\",
#  \"x-csrf-token\": \"dfbcdbb17c5df03a5228368032e240b124d734ae870a766cd1c9f6b420c516829096acb610bd8e6debfb9992ffd1eab061ad1bfdc7100ee7b25e23dee64e2edc4faa9acdc5a76d4772402d878dedeef8\",
#  \"x-twitter-active-user\": \"yes\",
#  \"x-twitter-auth-type\": \"OAuth2Session\",
#  \"x-twitter-client-language\": \"en\" 
# }

# payload = json.dumps({
#   \"variables\": {
#     \"tweet_id\": \"1646151432993746949\",
#     \"dark_request\": False
#   },
#   \"queryId\": \"ojPdsZsimiJrUGLR1sjUtA\"
# })

# response = requests.request(\"POST\", reqUrl, data=payload,  headers=headersList)

# print(response.text)