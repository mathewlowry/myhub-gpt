---
creation date: 2023-08-15 12:37
modification date: 227 August 2023 12:37:14
---
# RSS to AllNotes Prompt, created # 2023-08-15 12:37

Creates the AllNotes file from a MyHub Collection by processing the collection's RSS file.

## current version 3
v2 but shorter
```
I am going to give you some RSS items and you will process it as follows: 
1. Extract the title of the RSS item. 
2. Extract the URL from the <link> item, not the <guid> item, and removes any utm suffix 
3. Extract the main content from the description section, taking care to not remove any content from description 
4. Remove any HTML tags within the main content. 
5. Preserve line breaks for paragraph breaks. 
6. Present the extracted title followed by the cleaned main content. 

Here is an example input item: 
<item> 
<guid>https://myhub.ai/items/originals-hidden-brain-npr</guid> 
<pubDate>Mon, 03 Dec 2018 12:07:34 CET</pubDate> 
<title>Originals | Hidden Brain : NPR</title> 
<link>https://www.npr.org/2018/08/20/640216385/you-2-0-originals?utm_source=pocket_reader</link> 
<description>In his new book, Originals: How Non-Conformists Move the World, Adam investigates who comes up with great ideas, how, and what we can do to have more of them....<br> originals are not the people with the deepest expertise. They're people with the broadest experience... really good at questioning the status quo...<p>Tags: creativity, innovation, management, top3pods, original</p></description> <category>creativity</category> <category>innovation</category> <category>management</category> <category>top3pods</category> <category>original</category> 
</item> 

And here is how I'd like you to process it: 
Originals | Hidden Brain : NPR https://www.npr.org/2018/08/20/640216385/you-2-0-originals 
In his new book, Originals: How Non-Conformists Move the World, Adam investigates who comes up with great ideas, how, and what we can do to have more of them.... originals are not the people with the deepest expertise. They're people with the broadest experience... really good at questioning the status quo...

And now here is the content I want you to process:
```
## v2
* includes all instructions from v1
* removes utm suffix from URL
* specifies to not remove any content from description

```
I am going to give you some RSS items and you will process it as follows: 
1. Extract the title of the RSS item. 
2. Extract the URL from the <link> item, not the <guid> item, and removes any utm suffix 
3. Extract the main content from the description section, taking care to not remove any content from description 
4. Remove any HTML tags within the main content. 
5. Preserve line breaks for paragraph breaks. 
6. Present the extracted title followed by the cleaned main content. 

Here is an example input item: 
<item> 
<guid>https://myhub.ai/items/originals-hidden-brain-npr</guid> 
<pubDate>Mon, 03 Dec 2018 12:07:34 CET</pubDate> 
<title>Originals | Hidden Brain : NPR</title> 
<link>https://www.npr.org/2018/08/20/640216385/you-2-0-originals?utm_source=pocket_reader</link> 
<description>In his new book, Originals: How Non-Conformists Move the World, Adam investigates who comes up with great ideas, how, and what we can do to have more of them.... They often procrastinate, and that's how they incubate ideas.... Their parents focus more on values than rules... One of the risks is, you know, you have everybody marching in a different direction...They feel the same fears and doubts that the rest of us do. They just manage them differently. They hate taking risks. And they have lots of bad ideas, and that's how they get to the good ones....<br> originals are not the people with the deepest expertise. They're people with the broadest experience... really good at questioning the status quo... is a hallmark of being an original... <br> when they have an opportunity to dive head-first into something, take a big risk, they actually hedge their bets and hesitate.... the fear of failing gets overtaken by the fear of failing to try... shift from worrying about... making a fool of yourself to regretting never taking a chance.... in the long run our biggest regrets are our inactions - the chances we didn't take...<br> they are drafted by other people... what makes them so effective ... they've spent months or years stewing on these ideas. And they've hatched by the time that somebody pulls them into the spotlight... <br> originality is brewing in all sorts of unexpected places... who are the people that, you know, are in a position to bring really new ideas into this organization. And why aren't we hearing from them? ... there's zero correlation between who's the best talker and who has the best ideas... what distinguishes the great from the ordinary is ... the great simply have many more ideas than the ordinary... failed the most because they're the ones who tried the most....<br> a lot of us fall in love with our first ideas, and those are the most conventional... you have to weed out the familiar in order to get to the unusual. But a lot of people never get to those later ideas... it's just really hard to judge your own ideas.<p>Tags: creativity, innovation, management, top3pods, original</p></description> <category>creativity</category> <category>innovation</category> <category>management</category> <category>top3pods</category> <category>original</category> 
</item> 

And here is how I'd like you to process it: 
Originals | Hidden Brain : NPR https://www.npr.org/2018/08/20/640216385/you-2-0-originals 
In his new book, Originals: How Non-Conformists Move the World, Adam investigates who comes up with great ideas, how, and what we can do to have more of them.... They often procrastinate, and that's how they incubate ideas.... Their parents focus more on values than rules... One of the risks is, you know, you have everybody marching in a different direction...They feel the same fears and doubts that the rest of us do. They just manage them differently. They hate taking risks. And they have lots of bad ideas, and that's how they get to the good ones.... originals are not the people with the deepest expertise. They're people with the broadest experience... really good at questioning the status quo... is a hallmark of being an original... when they have an opportunity to dive head-first into something, take a big risk, they actually hedge their bets and hesitate.... the fear of failing gets overtaken by the fear of failing to try... shift from worrying about... making a fool of yourself to regretting never taking a chance.... in the long run our biggest regrets are our inactions - the chances we didn't take...<br> they are drafted by other people... what makes them so effective ... they've spent months or years stewing on these ideas. And they've hatched by the time that somebody pulls them into the spotlight... <br> originality is brewing in all sorts of unexpected places... who are the people that, you know, are in a position to bring really new ideas into this organization. And why aren't we hearing from them? ... there's zero correlation between who's the best talker and who has the best ideas... what distinguishes the great from the ordinary is ... the great simply have many more ideas than the ordinary... failed the most because they're the ones who tried the most.... a lot of us fall in love with our first ideas, and those are the most conventional... you have to weed out the familiar in order to get to the unusual. But a lot of people never get to those later ideas... it's just really hard to judge your own ideas. 

And now here is the content I want you to process:
```


## version  1

```

I am going to give you some RSS items and you will process it in the way I show you.

Here is an example input item:
<item>
<guid>https://myhub.ai/items/originals-hidden-brain-npr</guid>
<pubDate>Mon, 03 Dec 2018 12:07:34 CET</pubDate>
<title>Originals | Hidden Brain : NPR</title>
<link>https://www.npr.org/2018/08/20/640216385/you-2-0-originals</link>
<description>In his new book, Originals: How Non-Conformists Move the World, Adam investigates who comes up with great ideas, how, and what we can do to have more of them.... They often procrastinate, and that's how they incubate ideas.... Their parents focus more on values than rules... One of the risks is, you know, you have everybody marching in a different direction...They feel the same fears and doubts that the rest of us do. They just manage them differently. They hate taking risks. And they have lots of bad ideas, and that's how they get to the good ones....<br> originals are not the people with the deepest expertise. They're people with the broadest experience... really good at questioning the status quo... is a hallmark of being an original... <br> when they have an opportunity to dive head-first into something, take a big risk, they actually hedge their bets and hesitate.... the fear of failing gets overtaken by the fear of failing to try... shift from worrying about... making a fool of yourself to regretting never taking a chance.... in the long run our biggest regrets are our inactions - the chances we didn't take...<br> they are drafted by other people... what makes them so effective ... they've spent months or years stewing on these ideas. And they've hatched by the time that somebody pulls them into the spotlight... <br> originality is brewing in all sorts of unexpected places... who are the people that, you know, are in a position to bring really new ideas into this organization. And why aren't we hearing from them? ... there's zero correlation between who's the best talker and who has the best ideas... what distinguishes the great from the ordinary is ... the great simply have many more ideas than the ordinary... failed the most because they're the ones who tried the most....<br> a lot of us fall in love with our first ideas, and those are the most conventional... you have to weed out the familiar in order to get to the unusual. But a lot of people never get to those later ideas... it's just really hard to judge your own ideas.<p>Tags: creativity, innovation, management, top3pods, original</p></description>
<category>creativity</category>
<category>innovation</category>
<category>management</category>
<category>top3pods</category>
<category>original</category>
</item>

And here is how I'd like you to process it:
Originals | Hidden Brain : NPR
In his new book, Originals: How Non-Conformists Move the World, Adam investigates who comes up with great ideas, how, and what we can do to have more of them.... They often procrastinate, and that's how they incubate ideas.... Their parents focus more on values than rules... One of the risks is, you know, you have everybody marching in a different direction...They feel the same fears and doubts that the rest of us do. They just manage them differently. They hate taking risks. And they have lots of bad ideas, and that's how they get to the good ones....
originals are not the people with the deepest expertise. They're people with the broadest experience... really good at questioning the status quo... is a hallmark of being an original... 
when they have an opportunity to dive head-first into something, take a big risk, they actually hedge their bets and hesitate.... the fear of failing gets overtaken by the fear of failing to try... shift from worrying about... making a fool of yourself to regretting never taking a chance.... in the long run our biggest regrets are our inactions - the chances we didn't take...<br> they are drafted by other people... what makes them so effective ... they've spent months or years stewing on these ideas. And they've hatched by the time that somebody pulls them into the spotlight... <br> originality is brewing in all sorts of unexpected places... who are the people that, you know, are in a position to bring really new ideas into this organization. And why aren't we hearing from them? ... there's zero correlation between who's the best talker and who has the best ideas... what distinguishes the great from the ordinary is ... the great simply have many more ideas than the ordinary... failed the most because they're the ones who tried the most....
a lot of us fall in love with our first ideas, and those are the most conventional... you have to weed out the familiar in order to get to the unusual. But a lot of people never get to those later ideas... it's just really hard to judge your own ideas.

```

I then asked: "Please boil down the above instructions and list the rules you will follow" to which it replied:

Certainly, here are the simplified rules I will follow based on your instructions:

1. Extract the title of the RSS item.
2. Extract the main content from the description section.
3. Remove any HTML tags within the main content.
4. Preserve line breaks for paragraph breaks.
5. Present the extracted title followed by the cleaned main content.


