# W2 7 Pretraining an LLM

**Channel:** AI Thought   |   **Date:** 2023-12-20   |   **URL:** https://www.youtube.com/watch?v=YgLDAIrU3Kw

## Description

_No description provided._

## Transcript

Andrew Ng: Many of the LLMs we've been using have been previously trained, or we say pre-trained by some company, often by a big tech company. When should you pre-train your own model? This turns out to be so expensive that when in doubt, I would say probably don't do it. But let's take a deeper look.

Andrew Ng: Many teams have been pre-training general-purpose LLMs by learning from text on the internet. These efforts to train very large language models may cost tens of millions of dollars, need a large dedicated engineering team, take many months, and a huge amount of data. Many teams have been open-sourcing such models and that's been a fantastic contribution to the AI community. If you have the resources to pre-train models and maybe even open-source them, please by all means, make that contribution to AI. I think that could be fantastic. But for building a specific application, given the time and expense of pre-training a model from scratch, I think of this as often an option of last resort. It could help if you have a highly specialized domain and a lot of data. For example, Bloomberg is a company that offers software as well as media articles centered around financial services. Because of its access to a huge amount of text on finance, it trained BloombergGPT, which is Bloomberg's custom-built large language model, purpose-built for financial applications, and Bloomberg reported that compared to general-purpose LLMs that had learned mainly from internet data, this model does quite a bit better on processing financial text.

Andrew Ng: For many practical applications, unless you have a huge amount of resources and a huge amount of data, it may be more practical to start with an LLM that someone else had pre-trained, say a general-purpose LLM that's learned from a lot of internet data that someone has open-sourced, and then to fine-tune that to your own data. And that will often give pretty decent performance but in a much more economic way. Now, I am sincerely very grateful to the teams that have been putting a lot of resources into pre-training LLMs on a lot of text data on the internet and then open-sourcing them. And in fact, this gives us many different LLMs that we could choose from to use. In the next video, we'll actually take a look at the issue of what size LLM do you want to use and of all the different LLMs out there, how do you think about choosing among different ones? Let's go take a look at that in the next video.