# Email Newsletter Pipeline

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Active-brightgreen.svg)]()

A sophisticated, production-ready automated email newsletter processing and delivery system designed to streamline bulk newsletter distribution with advanced subscriber management, content processing, and delivery tracking.

## 🎯 Overview

The Email Newsletter Pipeline is an enterprise-grade solution that automates the end-to-end process of newsletter creation, segmentation, processing, and delivery. It provides a robust framework for managing subscriber data, processing content, and handling batch deliveries with comprehensive logging and audit trails.

## ✨ Features

- **Subscriber Management**: Advanced subscriber database with validation, segmentation, and preference management
- **Content Processing**: Intelligent content parsing and transformation for multiple formats
- **Batch Delivery**: Efficient batch-based email delivery system with configurable batch sizes
- **Database Management**: SQLite-based persistent storage with automated schema management
- **Audit Logging**: Comprehensive logging system for tracking all operations and delivery events
- **Error Handling**: Robust error handling with detailed error reporting and recovery mechanisms
- **Configuration Management**: Flexible configuration system for environment-specific settings
- **Data Export**: Generate detailed delivery reports and batch statistics

## 📋 Project Structure

```
Email_Newsletter_Pipeline/
├── input_newsletters/          # Source newsletter files (Markdown format)
│   ├── newsletter1.md
│   └── newsletter2.md
├── data/                       # Subscriber data and datasets
│   └── subscribers.csv
├── output/                     # Generated output files
│   ├── batches/               # Batch delivery files
│   └── reports/               # Delivery reports
├── logs/                       # Application logs and audit trails
│   └── audit.log
├── database/                   # Database files
│   └── newsletter.db
├── config.py                   # Configuration settings
├── main.py                     # Application entry point
├── content_processor.py        # Content parsing and processing
├── subscriber_manager.py       # Subscriber data management
├── delivery_manager.py         # Email delivery orchestration
├── database_manager.py         # Database operations
├── logger_setup.py            # Logging configuration
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- SQLite3 (typically included with Python)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/manishk30543-dev/Email-Newsletter-Pipeline.git
   cd Email-Newsletter-Pipeline
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Edit `config.py` to customize the following settings:

```python
# Database configuration
DB_PATH = 'database/newsletter.db'

# Batch processing settings
BATCH_SIZE = 50              # Number of subscribers per batch
MAX_RETRIES = 3              # Retry attempts for failed deliveries

# Logging configuration
LOG_LEVEL = 'INFO'
LOG_DIR = 'logs/'

# Input/Output paths
INPUT_DIR = 'input_newsletters/'
OUTPUT_DIR = 'output/'
```

## 📖 Usage

### Basic Operation

```bash
python main.py
```

### Processing Workflow

1. **Place newsletter files** in `input_newsletters/` directory (Markdown format)
2. **Ensure subscriber data** is available in `data/subscribers.csv`
3. **Run the pipeline**:
   ```bash
   python main.py
   ```
4. **Check output** in `output/` directory for batch files and reports
5. **Review logs** in `logs/audit.log` for detailed execution information

### Subscriber Data Format

CSV file with the following structure:
```csv
id,email,name,subscription_date,status
1,user@example.com,John Doe,2024-01-15,active
2,subscriber@domain.com,Jane Smith,2024-02-20,active
```

### Newsletter Format

Markdown files in `input_newsletters/` directory:
```markdown
# Weekly Newsletter - April 22, 2026

## Content Section

Your newsletter content goes here...

---

## Featured Articles

- Article 1
- Article 2
```

## 🏗️ Architecture

### Core Modules

- **main.py**: Orchestrates the entire pipeline workflow
- **config.py**: Centralized configuration management
- **content_processor.py**: Handles content parsing, validation, and transformation
- **subscriber_manager.py**: Manages subscriber data, validation, and segmentation
- **delivery_manager.py**: Orchestrates batch creation and delivery tracking
- **database_manager.py**: Handles all database operations and schema management
- **logger_setup.py**: Configures application logging

### Data Flow

```
Input Newsletter → Content Processor → Subscriber Manager → 
Delivery Manager → Batch Creator → Output Generation → 
Database Storage → Audit Logging
```

## 📊 Output

The pipeline generates:

- **Batch Files** (`output/batches/`): CSV files for each batch containing subscriber and content mapping
- **Delivery Reports** (`output/`): Summary reports with delivery statistics
- **Audit Logs** (`logs/audit.log`): Comprehensive operation logs with timestamps

## 🔧 Configuration Guide

### Batch Processing

Adjust batch size based on your email service provider limits:

```python
BATCH_SIZE = 50  # Adjust as needed
```

### Logging Levels

```python
LOG_LEVEL = 'DEBUG'    # Verbose logging
LOG_LEVEL = 'INFO'     # Standard logging
LOG_LEVEL = 'WARNING'  # Warning and errors only
LOG_LEVEL = 'ERROR'    # Errors only
```

## 📝 Error Handling

The system includes comprehensive error handling for:

- Invalid subscriber data
- Missing or malformed newsletter files
- Database connectivity issues
- File I/O errors
- Data validation failures

All errors are logged with full context for troubleshooting.

## 🧪 Testing

```bash
# Run with verbose logging for testing
python main.py --verbose
```

## 📦 Dependencies

See `requirements.txt` for all required packages. Key dependencies include:

- sqlite3 (database)
- csv (data processing)
- markdown (content processing)
- logging (audit trail)

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Manish Kumar**
- GitHub: [@manishk30543-dev](https://github.com/manishk30543-dev)
- Email: mansihk30543@gmail.com

## 🐛 Bug Reports & Feature Requests

Found a bug or have a feature idea? Please [open an issue](https://github.com/manishk30543-dev/Email-Newsletter-Pipeline/issues) on GitHub.

## 📮 Support

For support, questions, or suggestions, please reach out via:
- GitHub Issues
- Email: mansihk30543@gmail.com

## 🗺️ Roadmap

- [ ] Multi-format newsletter support (HTML, PDF)
- [ ] Advanced subscriber segmentation
- [ ] Real-time delivery tracking
- [ ] Email template library
- [ ] API interface for external integration
- [ ] Web dashboard for monitoring
- [ ] Scheduled newsletter automation

## 📚 Documentation

For detailed documentation on each module, see:
- [Content Processor Documentation](docs/content_processor.md)
- [Subscriber Manager Documentation](docs/subscriber_manager.md)
- [Delivery Manager Documentation](docs/delivery_manager.md)
- [Database Schema](docs/database_schema.md)

## ✅ Version History

- **v1.0.0** (April 22, 2026) - Initial release

---

**Last Updated**: April 22, 2026

Made with ❤️ by Manish Kumar
