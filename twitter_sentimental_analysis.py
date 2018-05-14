import tweepy,sys
from tweepy import OAuthHandler
from textblob import TextBlob
import matplotlib.pyplot as plt

def percentage(part,whole):
    return 100*float(part)/float(whole)

if __name__ =="__main__":
    
    consumer_key = "MPyNWgJ7KzUtebgMh2vWfuSjf"
    consumer_secret = "PqGfci55NJuDztI5wfFdvOF7wtJL6Hm60fGp9e8mQAzXCG2Npk"
    access_token = "136542236-W2Fvq9riCqUAWiZYcNO42xxOe3ONsCaig5afOlXB"
    access_token_secret = "UfxgtG6IMisv15EHz3KCFvsP6xrOtMDa82XdRZfGmwBae"

    auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)
    
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    
    search_term = input("Enter Keyword:")
    no_of_searched_terms = int(input("Enter the no of searches:"))

    tweets = tweepy.Cursor(api.search,q=search_term,lang="English").items(no_of_searched_terms)
    positive = 0
    negative = 0
    neutral = 0
    polarity = 0


    for tweet in tweets:
        print(tweet.text.translate(non_bmp_map))
        analysis = TextBlob(tweet.text)
        polarity+=analysis.sentiment.polarity

        if(analysis.sentiment.polarity == 0):
            neutral+=1
        elif(analysis.sentiment.polarity < 0.00):
            negative+=1
        elif(analysis.sentiment.polarity > 0.00):
            positive+=1
            
    positive = percentage(positive,no_of_searched_terms)
    negative = percentage(negative,no_of_searched_terms)
    neutral = percentage(neutral,no_of_searched_terms)

    positive = format(positive,'.2f')
    negative = format(negative,'.2f')
    neutral = format(neutral,'.2f')

    if(polarity == 0):
            print("Neutral Feedback")
    elif(polarity < 0.00):
            print("Negative Feedback")
    elif(polarity > 0.00):
            print("Positive Feedback")
            
    labels = ['Positive['+str(positive)+'%]','Neutral['+str(neutral)+'%]','Negative['+str(negative)+'%]']
    sizes = [positive,neutral,negative]
    colors = ['yellow','green','red']
    patches,texts = plt.pie(sizes,colors=colors,startangle=90)
    plt.legend(patches,labels,loc="best")
    plt.title('Peoples rating on the' +search_term )
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
    
