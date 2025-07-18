# Swing Momentum Algorithm

**Purpose:** This algorithm helps identify when a stock's price might change direction (swing up or down) to suggest potential buy or sell opportunities.

**Core Idea:** Stock prices tend to move in "swings" – going up for a while, then down, then up again. By finding recent highest and lowest points, we can predict the next short-term direction.

**Data Used:**

- Daily stock data (Open, High, Low, Close prices).
- We only look at the most recent **1 month** of this daily data (about 20-22 trading days).

---

### How the Algorithm Works (Step-by-Step):

1.  **Sliding Data Window:**

    - The algorithm always uses a fixed "window" of the last 1 month of daily data.
    - Every new day, the oldest day's data is removed, and the newest day's data is added. This keeps the window always focused on the recent past.

2.  **Determine Current Trend:**

    - **Find Extremes:** Within the 1-month window, identify:
      - The day with the **absolute highest price** (let's call it `HighDay`).
      - The day with the **absolute lowest price** (let's call it `LowDay`).
    - **Check Proximity:**
      - If `LowDay` is **closer** to today's date than `HighDay`, the trend is **Uptrend**. (Recent bottom suggests prices will go up).
      - If `HighDay` is **closer** to today's date than `LowDay`, the trend is **Downtrend**. (Recent peak suggests prices will go down).

3.  **Generate Buy/Sell Signals:**

    - **For an Uptrend (looking to BUY):**
      - If, on any day _after_ the `LowDay` (but before today), the stock's `Open` price was **very close to** the `Low` price of that `LowDay`.
      - **Signal:** If this happens, a **BUY** signal is generated for the _next_ trading day.
    - **For a Downtrend (looking to SELL):**
      - If, on any day _after_ the `HighDay` (but before today), the stock's `Open` price was **very close to** the `High` price of that `HighDay`.
      - **Signal:** If this happens, a **SELL** signal is generated for the _next_ trading day.
    - _(Note: "Very close to" means within a tiny percentage, as exact matches are rare.)_

4.  **Set Target and Stop-Loss:**

    - **If BUY Signal (Uptrend):**
      - **Target:** The `High` price of the `HighDay`.
      - **Stop-Loss:** The `Low` price of the `LowDay`.
    - **If SELL Signal (Downtrend):**
      - **Target:** The `Low` price of the `LowDay`.
      - **Stop-Loss:** The `High` price of the `HighDay`.
    - _(A "threshold" might be added to these prices later, requiring testing.)_

---

This algorithm runs daily, constantly updating its view of the 1-month data window to find new opportunities.
