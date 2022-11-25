# generalEsports

This project is a collection of the code, graphs and analyses that i've created while trying to answer some questions about the video games such as "Valorant" and "Counter-Strike Global Offensive" along with their esports domains

I've added a short description (question being answered, analysis methods used, conclusion, other thoughts) for each file


“ages.py”:
The question I tried to answer was to see if team age and world ranking were correlated. The reason I wanted to answer this question is because a lot of people claim youth is a very important factor in video games, but at the same time, experience is also key, so this was to see how the best teams were distributed in terms of age and experience. I wanted to look at how this distribution held up for a well established esport like CSGO’s and then compare it to a new esport like Valorant’s. 
I gathered data from HLTV.org along with VLR.GG, and using a simple scatter plot I plotted age versus world ranking (for valorant i just used how they did at stage 3, tiebreakers decided by h2h or round difference). I added a background picture to show the different “areas”, with some areas being “old but gold” and “young and upcoming”. 
The conclusion was that in a game like CSGO, it makes more sense to have young players with a medium amount of experience, whereas in Valorant it makes more sense to have experienced players rather than youth. I believe that this makes sense as a game like csgo requires a high level of mechanical skill, whereas in valorant, a game with much smaller mechanical skill gap, we see that experience matters most. 
I had a conversation with one of my viewers where they disagreed about how I represented my areas. They suggested that instead of hard zones, I should use a gradient instead, which I intend to do in a future video. I also think that it makes more sense to look at how teams are aged(old IGL, young talent vs a medium IGL/talent)
