# Main entry point for trend following strategy

import sys
from utils.logo import print_logo
from utils.logger import setup_logger
from config.loader import get_str

log = setup_logger(__name__)

def main():
    print_logo()
    print("TradeGeist - Trend Following Strategy")
    log.info("TradeGeist - Trend Following Strategy started")
    
    # Get run mode with fallback to DRYTEST if not found
    run_mode = get_str("run_mode", "DRYTEST").upper()
    log.info(f"RUN_MODE loaded from config: {run_mode}")
    
    if run_mode == "DRYTEST":
        from core.strategies.drytest_trend_following import start_drytest_trend_following
        start_drytest_trend_following()
    elif run_mode == "LIVE":
        from core.strategies.live_trend_following import start_live_trend_following
        start_live_trend_following()
    else:
        log.error(f"Unknown run mode: {run_mode}")
        print(f"Error: Unknown run mode: {run_mode}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nTradeGeist - Trend Following Strategy stopped by user")
        log.info("TradeGeist - Trend Following Strategy stopped by user")
    except Exception as e:
        print(f"Error: {str(e)}")
        log.error(f"Error: {str(e)}")
        sys.exit(1)