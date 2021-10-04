# reference:https://codelabs.developers.google.com/codelabs/cloud-natural-language-python3#6
from google.cloud import language


def entities_sentiment(doc):
    client = language.LanguageServiceClient()
    document = language.Document(content=doc, type_=language.Document.Type.PLAIN_TEXT)
    response = client.analyze_entity_sentiment(document=document,encoding_type='UTF32')
    res=client.analyze_sentiment(document=document,encoding_type='UTF32',)
    sentiment = res.document_sentiment
    fin = dict(
        sentence=doc,
        overallscore=f"{sentiment.score:.1%}",
        overallmagnitude=f"{sentiment.magnitude:.1%}",
    )
    print("overall sentiment: ")
    for key, value in fin.items():
        print(f"{key:15}: {value}")
    for entity in response.entities:
        print("-------------------------------------")
        results = dict(
            name=entity.name,
            type=entity.type_.name,
            salience=f"{entity.salience:.1%}",
            score=entity.sentiment.score,
            magnitude=entity.sentiment.magnitude
        )
        for key, value in results.items():
            print(f"{key:15}:  {value}")
