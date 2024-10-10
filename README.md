# AdMeneerV1

AdMeneerV1 is a local ad tracking system designed to detect and log advertisements (both audio and video) across various media channels (TV and radio).

## Prerequisites

- Node.js (v14 or later)
- Python (v3.7 or later)
- pip (Python package installer)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/admeneev1.git
   cd admeneev1
   ```

2. Install frontend dependencies:
   ```
   npm install
   ```

3. Install backend dependencies:
   ```
   pip install -r backend/requirements.txt
   ```

4. Create necessary directories:
   ```
   mkdir uploads
   mkdir recordings
   ```

## Running the Application

To run both the frontend and backend concurrently:

```
npm start
```

This will start the React development server on `http://localhost:5173` and the Flask backend on `http://localhost:5000`.

## Usage

1. Open your browser and navigate to `http://localhost:5173`.
2. Use the interface to manage ads, channels, and view detections.
3. The background process will continuously monitor the specified channels for ad detections.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.