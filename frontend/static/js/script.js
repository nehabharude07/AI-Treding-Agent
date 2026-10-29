
document.addEventListener("DOMContentLoaded", () => {
    const getElement = (...ids) =>
        ids.map(id => document.getElementById(id)).find(Boolean);

    const runBtn = getElement("runBtn");
    const statusElement = getElement("agentStatus");

    const showStatus = (message) => {
        if (statusElement) statusElement.textContent = message;
    };

    if (!runBtn) {
        console.error("Run Agent button not found. Check the button ID.");
        return;
    }

    // Prevent duplicate event listeners.
    if (runBtn.dataset.listenerAttached === "true") return;
    runBtn.dataset.listenerAttached = "true";

    runBtn.addEventListener("click", async () => {
        const readNumber = (...ids) => {
            const element = getElement(...ids);
            return element ? Number(element.value) : NaN;
        };

        const portfolio_value = readNumber("portfolioValue", "portfolio_value");
        const trade_size = readNumber("tradeSize", "trade_size");
        const open = readNumber("open");
        const high = readNumber("high");
        const low = readNumber("low");
        const close = readNumber("close");
        const volume = readNumber("volume");

        const values = [portfolio_value, trade_size, open, high, low, close, volume];

        if (values.some(value => !Number.isFinite(value))) {
            showStatus("Please enter valid numbers in all fields.");
            alert("Please enter valid numbers in all fields.");
            return;
        }

        if (portfolio_value <= 0 || trade_size <= 0) {
            showStatus("Portfolio value and trade size must be greater than zero.");
            return;
        }

        const originalText = runBtn.textContent;
        runBtn.disabled = true;
        runBtn.textContent = "Running...";
        showStatus("Sending data to the trading agent...");

        try {
            const response = await fetch("/run-agent", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    portfolio_value,
                    trade_size,
                    features: { open, high, low, close, volume }
                })
            });

            const result = await response.json();

            if (!response.ok) {
                const message = result.detail || result.error ||
                    `Request failed with status ${response.status}`;
                throw new Error(
                    typeof message === "string" ? message : JSON.stringify(message)
                );
            }

            const signalElement = getElement("signal");
            const returnElement = getElement("totalReturn");
            const sharpeElement = getElement("sharpe");

            if (signalElement) {
                signalElement.textContent = result.signal ?? "-";
            }

            if (returnElement) {
                returnElement.textContent =
                    result.profit ?? result.total_return ?? "-";
            }

            if (sharpeElement) {
                sharpeElement.textContent =
                    result.sharpe_ratio ?? result.sharpe ?? "N/A";
            }

            showStatus("Trading agent completed successfully.");
        } catch (error) {
            console.error("Run Agent error:", error);
            showStatus(`Error: ${error.message}`);
        } finally {
            runBtn.disabled = false;
            runBtn.textContent = originalText;
        }
    });
});
