Sometimes it can be really useful to understand which messages have negative or positive coloring. Especially if we’re talking about chat moderation. Instead of calling an admin (house chats are a sore topic!), it’s more convenient to enable automation of cleaning messages with a negative component, for example, insults or obscene language. So, this bot can be used for this aim.

Since I decided to work with the Russian language, the choice fell on the Dostoevsky python library. This model was trained on RuSentiment dataset and achieves up to ~0.71 F1 score.

So, lemmatization and stop-word removing depend on the specifics of your task. I decided not to use these two aspects. Moreover, Dostoevsky provides a model for sentiment-analysis that can work with raw texts. It means that you can transfer texts directly to the library without steps mentioned above.

However, lemmatization and stop-word removing can increase accuracy. If your task requires an accurate sentiment-analysis and you are dealing with a large amount of texts, in this case you should lemmatize and delete stop words before transferring texts to the Dostoevsky library. 

The Dostoevsky classifies the text into 5 classes:
- negative;
- positive;
- neutral;
- speech act (formal greetings, thank-you and congratulatory posts);
- the "skip" class is for unclear cases.

In this project I’m interested only in negative, positive and neutral classes. Also remember that Dostoevsky doesn’t consider emojis as a component of tonality.

Let’s have a look at the algorithm of sentiment-analyzer implemented as a telegram-bot.
[U<mxfile host="app.diagrams.net" modified="2023-06-29T15:59:12.399Z" agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" etag="SSHJF2adhxAnE2t5K9hm" version="21.3.6" type="google">
  <diagram name="Страница 1" id="I6u-tDR-h_s0eh76Tz8J">
    <mxGraphModel grid="1" page="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="MM9Sy5eRiMCl2AP7ZgGU-4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;fillColor=#dae8fc;strokeColor=#6c8ebf;" edge="1" parent="1" source="MM9Sy5eRiMCl2AP7ZgGU-1" target="MM9Sy5eRiMCl2AP7ZgGU-3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="MM9Sy5eRiMCl2AP7ZgGU-1" value="Installing dependencies (dostoevsky, python-telegram-bot) and downloading&amp;nbsp;fasttext-social-network-model" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="320" y="40" width="240" height="80" as="geometry" />
        </mxCell>
        <mxCell id="MM9Sy5eRiMCl2AP7ZgGU-10" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;fillColor=#dae8fc;strokeColor=#6c8ebf;" edge="1" parent="1" source="MM9Sy5eRiMCl2AP7ZgGU-3" target="MM9Sy5eRiMCl2AP7ZgGU-9">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="MM9Sy5eRiMCl2AP7ZgGU-3" value="Getting a bot token from BotFather (there&#39;re lots of guides in the Net)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="320" y="160" width="240" height="80" as="geometry" />
        </mxCell>
        <mxCell id="MM9Sy5eRiMCl2AP7ZgGU-13" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;fillColor=#dae8fc;strokeColor=#6c8ebf;" edge="1" parent="1" source="MM9Sy5eRiMCl2AP7ZgGU-5" target="MM9Sy5eRiMCl2AP7ZgGU-7">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="MM9Sy5eRiMCl2AP7ZgGU-5" value="Initializing the bot" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="320" y="400" width="240" height="80" as="geometry" />
        </mxCell>
        <mxCell id="MM9Sy5eRiMCl2AP7ZgGU-14" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;fillColor=#dae8fc;strokeColor=#6c8ebf;" edge="1" parent="1" source="MM9Sy5eRiMCl2AP7ZgGU-7" target="MM9Sy5eRiMCl2AP7ZgGU-8">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="MM9Sy5eRiMCl2AP7ZgGU-7" value="Launching the bot" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="320" y="520" width="240" height="80" as="geometry" />
        </mxCell>
        <mxCell id="MM9Sy5eRiMCl2AP7ZgGU-8" value="Testing the bot and enjoying the result!" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="320" y="640" width="240" height="60" as="geometry" />
        </mxCell>
        <mxCell id="MM9Sy5eRiMCl2AP7ZgGU-12" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;fillColor=#dae8fc;strokeColor=#6c8ebf;" edge="1" parent="1" source="MM9Sy5eRiMCl2AP7ZgGU-9" target="MM9Sy5eRiMCl2AP7ZgGU-5">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="MM9Sy5eRiMCl2AP7ZgGU-9" value="Message preprocessing (short-form: only tokenization with &quot;nltk&quot; and cleaning punctuaion with &quot;string&quot;)" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
          <mxGeometry x="320" y="280" width="240" height="80" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
ploading Алгоритм (2).drawio…]()


![sentiment-analyzer algorithm](https://github.com/NataliaKalinina13/sentiment_analyzer_bot/assets/85068191/0fbc7207-d473-4d6b-8a74-03e2ecb78abf)


And this is the result! Soon I’ll improve it and test new models, but now that’s it))
<img width="599" alt="image" src="https://github.com/NataliaKalinina13/sentiment_analyser_bot/assets/85068191/b4b5fe3a-72a1-4e77-946b-25a0f437e31f">



Don't forget to install requirements and download model weights for sentiment analysis (https://storage.b-labs.pro/models/fasttext-social-network-model.bin)

FastTextSocialNetworkModel.MODEL_PATH = '/<some_folders>/fasttext-social-network-model.bin' model = FastTextSocialNetworkModel(tokenizer=tokenizer)

