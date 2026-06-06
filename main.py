"""
Desktop Pet Application - Main Entry Point

A cute desktop pet that stays on top of your screen.
"""

import sys
import logging
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtCore import QTimer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pet.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def main():
    """Main entry point for the application."""
    
    logger.info("=" * 50)
    logger.info("Desktop Pet Application Starting")
    logger.info("=" * 50)
    
    # Create application
    app = QApplication(sys.argv)
    app.setApplicationName("Desktop Pet")
    app.setApplicationVersion("1.0.0")
    
    # Import after QApplication is created
    from src.ui.main_window import PetWindow
    from src.tray.system_tray import SystemTrayManager
    
    try:
        # Create main window
        window = PetWindow()
        window.show()
        
        # Create system tray
        tray = SystemTrayManager(app, window)
        
        # Connect tray signals
        tray.feed_pet.connect(window._on_feed)
        tray.play_pet.connect(window._on_play)
        tray.quit_requested.connect(window._on_quit)
        
        logger.info("Application initialized successfully")
        logger.info(f"Pet: {window.pet.name} ({window.pet.skin})")
        
        # Run application
        sys.exit(app.exec())
    
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
