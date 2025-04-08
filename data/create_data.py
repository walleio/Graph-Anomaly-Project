import os
import csv

users = []
reviews = []
review_number = 0
with open('movies.txt', 'r', errors='ignore') as file:
    user_dict = {}
    review_dict = {}
    for line in file:
        line = line.strip()
        if line.startswith('product/productId:'):
            review_dict['productId'] = line.split(': ', 1)[1]
        elif line.startswith('review/userId:'):
            review_dict['userId'] = line.split(': ', 1)[1]
            user_dict['userId'] = line.split(': ', 1)[1]
        elif line.startswith('review/profileName:'):
            # it is possible for there to be no profile name
            try:
                user_dict['profileName'] = line.split(': ', 1)[1].strip('"')  # Remove quotes
            except:
                user_dict['profileName'] = ''
        elif line.startswith('review/helpfulness:'):
            try:
                helpfulness = line.split(': ', 1)[1]
            except:
                helpfulness = '0/0' 
            
            review_dict['helpfulness numerator'] = int(helpfulness.split('/')[0])
            review_dict['helpfulness denominator'] = int(helpfulness.split('/')[1])
        elif line.startswith('review/score:'):
            review_dict['score'] = float(line.split(': ', 1)[1])
        elif line.startswith('review/time:'):
            review_dict['time'] = int(line.split(': ', 1)[1])
        elif line.startswith('review/summary:'):
            try:
                review_dict['summary'] = line.split(': ', 1)[1]
            except:
                review_dict['summary'] = ''
        elif line.startswith('review/text:'):
            review_dict['text'] = line.split(': ', 1)[1]
        
        if line == '':
            if user_dict not in users:
                users.append(user_dict)
            reviews.append(review_dict)
            user_dict = {}
            review_dict = {}

            '''
            if len(data) % 100000 == 0: 
                fieldnames = data[0].keys()
                file_exists = os.path.isfile('final_output.csv')

                with open('final_output.csv', 'a', newline='', encoding='utf-8') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                                    
                    # Write the column headers
                    if not file_exists:
                        writer.writeheader()
                                        
                    # Write each row
                    for row in data:
                        writer.writerow(row)
                    
                data = []
                break
            '''

            user_ratings = []
            if len(users) == 1000:
                for movie in reviews:
                    if len(user_ratings) == 0 or movie['userId'] not in [item['userId'] for item in user_ratings]:
                        user_ratings.append({'userId': movie['userId'], 
                                                'helpful ratings': movie['helpfulness numerator'], 
                                                'total ratings': movie['helpfulness denominator']})
                    else:
                        for rating in user_ratings:
                            if rating['userId'] == movie['userId']:
                                rating['helpful ratings'] = rating['helpful ratings'] + movie['helpfulness numerator']
                                rating['total ratings'] = rating['total ratings'] + movie['helpfulness denominator']

                filtered_list = list(filter(lambda r: r['total ratings'] >= 20, user_ratings))

                for l in filtered_list:
                    l['label'] = 1
                    average_rating = l['helpful ratings'] / l['total ratings']
                    if average_rating > 0.7:
                        l['label'] = 2
                    if average_rating < 0.3:
                        l['label'] = 0

                for i in users:
                    i['label'] = [j['label'] for j in filter(lambda x: x['userId'] == i['userId'], filtered_list)]

                filtered_reviews = []
                for i in reviews:
                    label = [j['label'] for j in filter(lambda x: x['userId'] == i['userId'], filtered_list)]
                    if label != []:
                        filtered_reviews.append(i)
                
                with open('users.csv', 'w', newline='', encoding='utf-8') as csvfile:
                    fieldnames = users[0].keys()
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                                        
                    for row in users:
                        if row['label'] != []:
                            row['label'] = row['label'][0]
                            writer.writerow(row)

                with open('reviews.csv', 'w', newline='', encoding='utf-8') as csvfile:
                    fieldnames = reviews[0].keys()
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()

                    for row in filtered_reviews:
                        writer.writerow(row)

                break
