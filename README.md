# HexOptiverChallenge2021
Optiver Challenge @ Hex Cambridge Hackathon 2021
Draft files contains a whole host of options we tried during the hackathon 

## Inspiration
Although exchanges across the globe have very much sorted day to day arbitrage differences between equities pricing differences, newer markets (e.g. crypto) will always provide opportunities to exploit these price variations on an instrument or instrument pair. Both market makers, brokers, and retail traders can exploit these arbitrage opportunities. This sounded very exciting to us and we decided to come up with a financial algorithm to address the challenge presented.

## What it does
We initially brainstormed various ideas for how these algorithms would work and how we could pick out these arbitrage opportunities in the market. Upon implementation we further expanded these algorithms over the course of the 36 hours.
We first laid the groundwork of what our algorithms had to follow:
Given that we were trading between liquid and illiquid markets, there would be many good entry points into the market on either side. As the volumes are different, we could act as a market maker in the illiquid market - provided that we could unload our positions quickly and successfully.
The tradeoffs were that we should not try to close every trade at a profit. We should focus on making a net profit and not winning every trade. We should take many short-term low volume entries and exit the market just as quick as we entered (akin to a sparrow pecking at food). We should focus on making more money of commissions than buying/selling shares and holding them (this is the job of a market maker). We should have no directional bias as we assumed (from empirical observation) that the markets were mostly flat.
The series of strategies we outlined include:
1. Comparing the two prices in different markets using conditions and inequalities to identify potential arbitrage opportunities.
2. Limit the number of positions we take on one side (this is done in order to limit our market exposure and keep our delta low.)
3. Take the same position volume as a hedge (so we can keep track and allow for more efficient clearing/unloading of positions.)
4. Limit the volume that we enter and exit with (e.g split a 20 lot trade into smaller 3 lot chunks). This ensures our order is filled and we enter the market quickly. Having a small lot size makes it easier to clear positions and decreases risk.
5. Our clearing strategy was the strategy we tweaked the most. We first ran into problems as our net delta and net positions were 0 but we were holding huge position sizes on the buy and sell side. Our clearing strategy was mostly based on bounding our trades with limit orders based on mean reversion of the bid and ask prices (see challenges section for more info). Unfortunately we were unable to implement a viable clearing strategy and this resulted in big losses despite making profits of arbitrage opportunities. 
6. Setting up a Circuit breaker so that no more trades are taken in a particular direction if 400 trades are reached. This is to prevent us reaching the cap on holding 500 positions in a given side.
7. Instead of taking prices at the lowest given price, we can undercut the market (at the expense of potentially more profit) to take a fixed amount of consistent profit. Outbidding the market in this way will allow us to enter the market before other participants.
8. We also tried to experiment strategy of how we could do the opposite of what everyone else was doing in terms of strategy to see how that worked too.

## How we built it
We used Python to build the algorithms.

## Challenges we ran into
We made many mistakes and encountered many obstacles with the code, but through addressing these we learnt a lot. Here are some of the obstacles we encountered / ideas we tried but couldn't implement in time:
1. Logs - we really should have had a more efficient way to track our attempts trading into the market and by outputting what trades we took and by attaching a label of which strategies were used in that trade we could more efficiently analyse the performance of our algorithm and see what was working and what was not.
2. Implementation - we encountered many bugs to in order to mitigate this we should have had checkers/flags to make sure each block of code works.
3. We tried to implement the following strategy but to no avail: Upon taking a pair of trades, we trade 4 limit orders - 2 bounding each bid/ask above and below - and once a limit order is filled the other corresponding one is cancelled. e.g if we enter the market with Bid price at 70, we open 2 limit orders at 69 and 71 so we limit our loss. If the market moves down we sell at 69 (at a slight loss) and the limit order at 71 is cancelled. This way we are protected from big moves against our position and we clear our open positions regularly.

## Accomplishments that we're proud of
We wrote a working code that can trade stocks and make a profit. And used the time to try numerous strategies and really there were so many ideas to try and experiment with. Given that we were not very experienced at python and this was the first-ever live programming project for some of our team I'd say we were very happy to have been able to implement the ideas we thought of in code to a good degree of success. We just wish we could have the env for longer to play around with and try different things.

## What we learned
We learnt a lot from our mistakes! We were really persistent and had a good crack at trying to solve the problems we encountered. We learnt a lot about structuring our logic and some more complex implementation in python.

## What's next for Optiver Market Maker
Fine-tuning the ideas and code to make the algorithm more successful. Mainly need to address the clearing of trades. Looking forward to taking part in future challenges from Optiver and in future Hackathons! Thanks to Optiver for providing a great platform and challenge for a very fun 36 hours of programming!


-Gorak
