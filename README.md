# Atlanta Train Tracker Backend

A FastAPI-based backend service that provides real-time Atlanta train data through a RESTful API for a future mobile application. This service polls train and prediction data from external APIs and serves cached results to minimize API calls and improve response times for mobile clients.

## Features

- Real-time train tracking data for Atlanta public transit system
- Cached data with automatic background updates every 10 seconds
- Optimized for mobile app consumption with fast response times
- RESTful API designed for mobile application integration
- CORS-enabled for cross-platform mobile frameworks
- Docker containerization for easy deployment and scaling
- FastAPI with automatic API documentation for mobile developers

## API Endpoints

### GET `/`
Returns a welcome message and API information.

**Response:**
```json
{
  "message": "Atlanta Train Tracker API"
}
```

### GET `/trains`
Returns cached train and prediction data.

**Response:**
```json
{
  "trains": [...],
  "predictions": [...],
  "last_updated": 1234567890
}
```

## Quick Start

⚠️ **Development Status: This project is currently under active development and is not ready for production use.**

### Current Status
- ✅ Basic API structure implemented
- ✅ Train data polling and caching system
- ✅ Docker containerization setup
- ❌ Deployment not ready
- ❌ Mobile app integration not implemented

### Development Environment
- Python 3.12+
- FastAPI framework
- Docker for containerization

## Project Structure

```
atl-train-tracker-backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application and routes
│   ├── atlanta_trains.py    # Train data polling and caching logic
│   └── links.py             # Environment variable configuration
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile              # Docker container configuration
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## Architecture

### Data Flow
1. **External APIs**: The backend connects to Atlanta public transit APIs for real-time data
2. **Background Polling**: A daemon thread polls these APIs every 10 seconds
3. **In-Memory Cache**: Retrieved data is cached with timestamps for fast access
4. **REST API**: FastAPI serves cached data through RESTful endpoints
5. **Mobile Ready**: Designed for consumption by a mobile application

### Key Components
- **`main.py`**: FastAPI application setup and route definitions
- **`atlanta_trains.py`**: Core polling logic and data caching mechanisms
- **`links.py`**: Environment variable management for API endpoints
- **Docker Setup**: Containerization for deployment flexibility

## Technical Specifications

### API Response Format
The `/trains` endpoint returns structured data containing:
- **trains**: Array of current train positions and status
- **predictions**: Array of arrival predictions for stations
- **last_updated**: Unix timestamp of last successful data fetch

### Performance Characteristics
- **Response Time**: < 100ms (served from cache)
- **Update Frequency**: 10-second intervals
- **Data Freshness**: Always within 10 seconds of source
- **Availability**: Too early to tell

## How It Works

1. **Background Polling**: The application starts a background thread that continuously polls the external train APIs every 10 seconds
2. **Data Caching**: Retrieved data is stored in memory cache with timestamp to reduce latency for mobile clients
3. **API Serving**: The FastAPI endpoints serve the cached data, ensuring fast response times crucial for mobile user experience
4. **Error Handling**: Failed API calls are logged but don't crash the service, maintaining reliability for mobile apps
5. **Mobile Optimization**: Lightweight JSON responses optimized for mobile data consumption

## Development Roadmap

### Phase 1: Basic fuctionalty (Complete)
- [x] Basic FastAPI application structure
- [x] Data polling and caching system
- [x] Docker containerization


### Phase 2: Improvements (Planned)
- [ ] API endpoint validation and testing
- [ ] Error handling improvements
- [ ] Environment configuration finalization

## Mobile App Integration

### Planned Mobile Features
- Real-time train tracking with live updates
- Station-specific arrival predictions


