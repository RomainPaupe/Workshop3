# Workshop3
Decentralization Technologies - workshop 3

# Team Member
- Romain PAUPE
- Thoams
- Valentin
- Noëmie

# Model Betting Game

Welcome to **Model Betting Game**, the ultimate competition where programmers bet on their machine learning models' predictive power to earn virtual money!

## Objective

Your goal is simple: Create the best predictive model and let it compete against others. The more accurate your predictions, the more money your model earns. But be careful—bad predictions will cost you! The competition never stops, and only the best models will thrive.

## Game Rules

1. **Starting Balance**: Each model starts with **€1000**.
2. **Prediction Rounds**: For each round, all models predict an outcome based on the same input data.
3. **Weight Influence**: Models have a **weight** that determines how much influence their predictions have on the final decision.
4. **Earnings and Losses**:
   - Models that predict closer to the weighted mean earn money.
   - Models that deviate too much lose money.
   - Lost money is redistributed to better-performing models, ensuring no money disappears from the system.
5. **Dynamic Weight Update**: The weight of each model is adjusted dynamically based on its past performance, using an error-based calculation.

## How the Weights are Calculated

- The weighted mean prediction is calculated using the formula:
  \(\text{Weighted Mean} = \frac{\sum (\text{predictions} \times \text{weights})}{\sum \text{weights}}\)
- Errors are calculated as:
  \(\text{Error} = |\text{Prediction} - \text{Weighted Mean}|\)
- New weights are updated using:
  \(\text{New Weight} = e^{-\text{Error}}\)
- A smoothing factor is applied to prevent drastic changes, and weights are normalized.

## Program transparency

You can find the complet program on this project with a output example


Ready to put your model to the test? Let the betting begin! 

