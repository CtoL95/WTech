# WTECH
Algorithmic trading repository


Build your ideal state strategy. Where if in this state you will earn as much as possible.
Detect market state and opponent positions. - Because in general you're just playing against the market, but you're also playing against specific opponents.
Match market state with tactic to progress towards strategic goal points. - For each market state, there's a series of actions you can perform to go to your ideal state.
Decide on counter-measure or alignment-measure. - Depending on whether you're progressing towards your ideal state or moving away, you can take actions to move towards it again. a. If counter-measure, decide on size, direction, time and method b. If alignment-measure, decide on size, direction, time and method.
Proceed to optimal execution, considering market impact, timing and cost. - To best progress towards your ideal state, you can try to minimize cost or consider the best steps.
possible improvements

Run Leveraged trades
Run options, futures and swaps
Run multiple asset types: Crypto, equity, derivatives, commodities
Algorithmic trading on medium time horizons
HFT - market making
Investing and venture capital on a long time horizon
Banking insurance and pension
Robotics, IT and resource development
energy
Macrostrategy
Detect Market state
What is the current trend state?
Question:
How precise is the mean return functional at detecting the trend?
How precise is the positive-negative functional at detecting the trend?
How precise is the battery of statistical tests at detecting the trend?

What is the current risk state?
Question:
What's the current volatility states?
What's the current connectability in the market?
What are the current probability states?

Has an extremal event occured?
Question:
How precise is Bollinger bands of 1.5, 2 or 2.5 sigma at detecting Extremal events?
How precise is the 10%, 5% and 1% quantile of xyz-interval returns at detecting Extremal events?
How precise is the 10%, 5% and 1% quantile of xyz-interval prices at detecting Extremal events?

Match corresponding strategy
If Up trend:
run long between 0-tangents, to minimize risk of loss
Check for Extremal events
If Negative Extremal event occurs - Close trades, take loss. Halt trading
If Positive Extremal event occurs - Close trades, take profit. Gauge trading
Check for Divergence and weight of closed trades.
If open, high and low diverge over time.
Consider whether a high volatility period is ahead and how to benefit on buying low and selling high.
If the the weight of the closing trades are significant and a certain direction has been chosen.
Consider whether to play along the direction or to take profit before a direction change.
Check for moment and moment drift
If Down trend:
run short between 0-tangets, to minimize risk of loss
Check for Extremal events
If Negative Extremal event occurs - Close trades, take loss. Halt trading
If Positive Extremal event occurs - Close trades, take profit. Gauge trading
Check for Divergence and weight of closed trades.
If open, high and low diverge over time.
Consider whether a high volatility period is ahead and how to benefit on buying low and selling high.
If the the weight of the closing trades are significant and a certain direction has been chosen.
Consider whether to play along the direction or to take profit before a direction change.
Check for moment and moment drift
If Flat trend:
run long between 0-tangents, to minimize risk of loss
run short between 0-tangets, to minimize risk of loss
Check for mean reversion indications
If the 6, 20 and 40 day moving averages cross
If the average directional index changes
If the trend indicators change
If the autocorrelation indicator increases
Check for Resistance levels If the Price reaches a previous resistance level - concrete price If the price reaches a fibonacci level - mythical & mystical price level If the price drops by x% from a previous max or min
Check for Breakthrough signals Unsure how to check this at the moment
If unknown trend:
Wait till a clear trend manifests
Implement trading strategy
If - Up trend
Entry:
Exit:

If - Down trend
Entry:
Exit:

If - Flat trend
Entry:
Exit:

If - Extremal event
Entry:
Exit:

Optimal executions
Up trend
Entry:
Exit:

Down trend
Entry:
Exit:

Flat trend
Entry:
Exit:

Research
DATASET - Price Timestamp+Date Open High Low Close Volume Returns_C

DATASET - Options

Markov model/Decision Tree Research
Goal: Determine the sign of tomorrows return, from today's Markov State.

Train the model on n > 25 datasets.
a. Sort dataset by conditions. for us this is up MA-cross and down MA-cross - This has to be researched further.
b. Add column with "Up" or "Down" indicators. Indicating the sign of the day's return.
c. Add column with indicator combinations of 3 and 5, such as "UUU", "DDD" and "UUUUU", "DDDDD".
d. Calculate the probabilities of next day return signs for each indicator combination.
Test the model, with the goal of achieving x >= 65% accuracy.
a. The current mean accuracy is 55% ...
If the result is x < 65% -> than there exists hidden variables. a. There must exist hidden variables, unaccounted for in moving averages
Hidden Markov model Research
Goal: Determine the trend, volatility, acceleration and sentiment states for tomorrow.
From a dataset on an asset. Determine the combined state for each timestep.
Question: How will I make the system decide on a given state?
Given 4 trends states: Up, Down, Flat, Unknown.
Given 4 volatility states: Extreme, high, medium, low.
Given 4 acceleration states: increasing, decreasing, neutral, Unknown.
Given 4 sentiment states: Positive, Negative, Neutral, Unknown.

Mean reversion Research
Goal: For periods where Mean Reversion is valid, what is the best method for earning?
What method is best at predicting mean reversions?

MA5, MA20, MA40
MACD
A combination?
Convergence Theorem Research
Goal: Determine the convergence or divergence states for high, low and close prices

Calculate convergence or divergence of highs
Calculate convergence or divergence of lows
Calculate convergence or divergence of close

What can this be used for? Market states, 0-tangents?
Linear Regression Research
Standard Deviation Research
Can you always or nearly always expect an opposite and equal force, when experiencing an 2-sigma, 2.5-sigma or 3-sigma event?

Mean Field Games Research
Technical Indicators Research
Expectation Maximation Research
0-tangent Research
How do i best measure 0-tangents, vendetangenter?

f(x) = Price f'(x) = returns f'(x) = 0?

Event based HFT
When Token X goes from Pumpfun to Raydium. Buy with HFT and sell. Pumpfun raydium? dexscanner Jito fees? spamming/crowding

Sandwich/MEV bot

KuCoin

Other
lgb, xgb, catboost https://www.kaggle.com/code/aimind/bottleneck-encoder-mlp-keras-tuner-8601c5

Cross-Validation (CV) Strategy and Feature Engineering:

5-fold 31-gap purged group time-series split Remove first 85 days for training since they have different feature variance Forward-fill the missing values Transfer all resp targets (resp, resp_1, resp_2, resp_3, resp_4) to action for multi-label classification Use the mean of the absolute values of all resp targets as sample weights for training so that the model can focus on capturing samples with large absolute resp. During inference, the mean of all predicted actions is taken as the final probability Deep Learning Model:

Use autoencoder to create new features, concatenating with the original features as the input to the downstream MLP model Train autoencoder and MLP together in each CV split to prevent data leakage Add target information to autoencoder (supervised learning) to force it to generate more relevant features, and to create a shortcut for backpropagation of gradient Add Gaussian noise layer before encoder for data augmentation and to prevent overfitting Use swish activation function instead of ReLU to prevent ‘dead neuron’ and smooth the gradient Batch Normalisation and Dropout are used for MLP Train the model with 3 different random seeds and take the average to reduce prediction variance Only use the models (with different seeds) trained in the last two CV splits since they have seen more data Only monitor the BCE loss of MLP instead of the overall loss for early stopping Use Hyperopt to find the optimal hyperparameter set

https://www.kaggle.com/competitions/optiver-realized-volatility-prediction/discussion/274970 https://www.kaggle.com/competitions/optiver-trading-at-the-close/discussion/487446 https://www.kaggle.com/competitions/jane-street-market-prediction/discussion/224348
