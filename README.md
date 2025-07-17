# Swing Momentum Algorithm for Short-Term Price Reversal Detection

**Author:** JAY

---

### Abstract

This paper introduces the "Swing Momentum" algorithm, a novel technical analysis approach designed to identify short-term price reversal opportunities in equity markets. Operating on a fixed 1-month (approx. 20-22 trading days) sliding window of daily Open, High, Low, and Close (OHLC) price data, the algorithm first determines the prevailing short-term trend by assessing the proximity of the most recent significant high or low within the lookback period. Subsequently, it generates buy or sell signals based on specific open price confirmations relative to these identified extreme points. The algorithm also proposes a dynamic methodology for setting target and stop-loss levels based on these historical highs and lows. While the core logic is presented, further empirical validation and optimization of parameters, particularly the tolerance for price equality and target/stop-loss thresholds, are necessary for practical application.

---

### 1. Introduction

The financial markets are characterized by inherent volatility and cyclical price movements. A widely observed phenomenon is the "swing" nature of asset prices, wherein periods of upward movement are typically followed by downward corrections, and vice-versa. Identifying the inflection points of these swings is a central objective for many short-term trading strategies. Traditional technical analysis relies on various indicators, such as moving averages, Relative Strength Index (RSI), and MACD, to gauge momentum and potential reversals.

This paper proposes a unique approach, the "Swing Momentum" algorithm, which deviates from conventional indicator-based methods by focusing directly on the recent extremes (highest high and lowest low) within a defined lookback period. The underlying hypothesis is that the proximity of a recent price extreme signals the likelihood of a reversal in the opposite direction. For instance, if a stock recently hit its lowest point within a month, it is hypothesized to be poised for an upward swing. This method aims to capture these anticipated movements by identifying specific price action confirmations.

The subsequent sections detail the methodology, including data requirements, trend determination, signal generation, and risk management (target and stop-loss setting). The paper concludes with a discussion of the algorithm's inherent limitations and outlines avenues for future research and empirical validation.

---

### 2. Methodology: The Swing Momentum Algorithm

The Swing Momentum algorithm operates on daily OHLC (Open, High, Low, Close) price data for a single equity. Its operational cycle involves continuous data window management, dynamic trend identification, and conditional signal generation.

#### 2.1 Data Management and Lookback Window

The algorithm employs a fixed-size **sliding window** of approximately **one calendar month** of daily trading data. Given typical market trading days, this translates to roughly **20-22 consecutive trading days**.

- As a new day's OHLC data becomes available, it is appended to the window.
- Concurrently, the oldest day's data is removed from the window, ensuring the lookback period remains constant and reflective of the most recent price action.

#### 2.2 Trend Determination Mechanism

The core of the trend identification process lies in assessing the recency of extreme price points within the 1-month lookback window.

- **2.2.1 Identification of Historical Extremes:**

  - **HighDay ($D_{H}$):** Identify the specific trading day within the current 1-month window where the absolute `High` price reached its maximum value.
  - **LowDay ($D_{L}$):** Identify the specific trading day within the current 1-month window where the absolute `Low` price reached its minimum value.

- **2.2.2 Proximity-Based Trend Classification:**
  - Let $N_{H}$ be the number of trading days elapsed between $D_{H}$ and the `CurrentDate` ($D_{C}$).
  - Let $N_{L}$ be the number of trading days elapsed between $D_{L}$ and the `CurrentDate` ($D_{C}$).
  - The `CurrentTrend` is then classified as follows:
    - **Uptrend:** If $N_{L} < N_{H}$. This implies that the most recent extreme was a low point, suggesting a potential upward price reversal or continuation.
    - **Downtrend:** If $N_{H} < N_{L}$. This implies that the most recent extreme was a high point, suggesting a potential downward price reversal or continuation.

#### 2.3 Signal Generation Logic

Trade signals are generated prospectively, targeting execution on the day _following_ the identification of specific trigger conditions.

- **2.3.1 Buy Signal (for Uptrend Confirmation):**

  - **Prerequisite:** The `CurrentTrend` must be classified as **Uptrend**.
  - **Trigger Condition:** The algorithm continuously monitors the `Open` price of recent trading days within the lookback window. A **Buy Trigger** is activated on a specific day, $D_{T}$, if its `Open` price is precisely equal to the `Low` price recorded on $D_{L}$ (the `LowDay` identified in Section 2.2.1).
    $$Open_{D_{T}} = Low_{D_{L}}$$
  - **Signal Issuance:** If the Buy Trigger condition is met on $D_{T}$, a **BUY signal** is issued for execution at the opening of the subsequent trading day, $D_{T+1}$.

- **2.3.2 Sell Signal (for Downtrend Confirmation):**
  - **Prerequisite:** The `CurrentTrend` must be classified as **Downtrend**.
  - **Trigger Condition:** Similar to the buy signal, the algorithm monitors `Open` prices. A **Sell Trigger** is activated on a specific day, $D_{T}$, if its `Open` price is precisely equal to the `High` price recorded on $D_{H}$ (the `HighDay` identified in Section 2.2.1).
    $$Open_{D_{T}} = High_{D_{H}}$$
  - **Signal Issuance:** If the Sell Trigger condition is met on $D_{T}$, a **SELL signal** is issued for execution at the opening of the subsequent trading day, $D_{T+1}$.

#### 2.4 Risk Management: Target and Stop-Loss Levels

Upon trade execution, predefined target and stop-loss levels are established based on the identified historical extremes.

- **2.4.1 For Buy Trades (Uptrend):**

  - **Profit Target ($TP_{B}$):** The `High` price of $D_{H}$ (the highest high within the 1-month window).
  - **Stop-Loss ($SL_{B}$):** The `Low` price of $D_{L}$ (the lowest low within the 1-month window).

- **2.4.2 For Sell Trades (Downtrend):**

  - **Profit Target ($TP_{S}$):** The `Low` price of $D_{L}$ (the lowest low within the 1-month window).
  - **Stop-Loss ($SL_{S}$):** The `High` price of $D_{H}$ (the highest high within the 1-month window).

- **2.4.3 Threshold Parameter:** It is hypothesized that a configurable threshold (e.g., a percentage buffer) may be applied to these calculated T/SL levels to optimize performance and account for market microstructure. This parameter requires empirical calibration through backtesting.

---

### 3. Results (Placeholder for Future Empirical Validation)

This section would typically present the results of extensive backtesting, including:

- Profitability metrics (e.g., net profit, profit factor, win rate).
- Risk metrics (e.g., maximum drawdown, average loss).
- Sensitivity analysis of the "Threshold Parameter" for T/SL.
- Performance across different market conditions (e.g., bull, bear, volatile, ranging).
- Examples of generated signals and corresponding trade outcomes.

---

### 4. Discussion of Limitations

While the Swing Momentum algorithm presents an intuitive approach to short-term swing trading, several critical limitations must be acknowledged:

1.  **Strict Equality Condition:** The requirement for `Open` price to _exactly_ match $High_{D_{H}}$ or $Low_{D_{L}}$ is extremely stringent. Real-world price data, particularly with high precision, rarely exhibits such exact matches. This could lead to a very low frequency of signals, potentially rendering the algorithm impractical. Introducing a small tolerance or epsilon ($\epsilon$) for price comparison ($|Open_{D_{T}} - ExtremePrice| < \epsilon$) is crucial for practical implementation.
2.  **Lookback Period Sensitivity:** The fixed 1-month lookback period is a critical parameter. Its optimality for various assets or market regimes is unknown and requires thorough investigation. Different lookback periods might yield significantly different results.
3.  **No Volume Consideration:** The algorithm solely relies on price action and does not incorporate trading volume, which is often a key indicator of conviction behind price movements.
4.  **Slippage and Execution Assumptions:** The assumption of trade execution at the next day's opening price does not account for real-world slippage, especially during volatile market openings or for illiquid stocks.
5.  **Lack of Market Context:** The algorithm operates on a single stock in isolation and does not incorporate broader market sentiment, sector performance, or fundamental news, which can significantly influence price movements.
6.  **"Previous Day" Trigger Ambiguity:** Clarification is needed regarding the specific Day X or Day Y (referred to as $D_{T}$) that triggers the signal. Is it any day after $D_{H}$/$D_{L}$ and before $D_{C}$ that meets the `Open = Extreme` condition? Or is it specifically the day immediately following $D_{H}$/$D_{L}$? The current interpretation assumes any such day within the sliding window.
7.  **Overfitting Risk:** Without rigorous out-of-sample backtesting, there is a risk of overfitting the algorithm to historical data, leading to poor performance in live trading.
8.  **Edge Cases:** Scenarios where $D_{H}$ and $D_{L}$ are the same day, or where extreme price movements render the T/SL levels impractical, need to be explicitly addressed.

---

### 5. Conclusion and Future Work

The Swing Momentum algorithm offers a direct and intuitive method for identifying potential short-term price reversals based on the recency of price extremes. Its simplicity in defining trend and signal conditions makes it a compelling subject for further research.

Future work should prioritize:

1.  **Empirical Backtesting and Optimization:** Conduct extensive historical backtesting across a diverse range of equities and market conditions. This is essential for:
    - Quantifying profitability and risk.
    - Optimizing the "Threshold Parameter" for T/SL.
    - Evaluating the impact of different lookback periods for the sliding window.
    - Determining an optimal $\epsilon$ for the `Open = Extreme` condition.
2.  **Robustness Testing:** Analyze the algorithm's performance sensitivity to data noise, missing data, and variations in execution prices.
3.  **Incorporation of Volume:** Investigate if incorporating volume data can enhance signal accuracy or filter out false signals.
4.  **Multi-Asset and Portfolio Management:** Extend the algorithm to a portfolio of stocks and explore strategies for capital allocation and risk diversification.
5.  **Real-Time Application:** Develop a system for real-time data acquisition and signal generation for potential live trading.
6.  **Comparative Analysis:** Compare the performance of Swing Momentum against established short-term trading strategies or benchmarks.

By addressing these areas, the potential efficacy and practical applicability of the Swing Momentum algorithm can be thoroughly assessed.
