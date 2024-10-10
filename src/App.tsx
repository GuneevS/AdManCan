import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { Home, LayoutDashboard, Radio, Tv, Settings } from 'lucide-react';
import ErrorBoundary from './components/ErrorBoundary';
import HomeDashboard from './components/HomeDashboard';
import AdsManagement from './components/AdsManagement';
import ChannelsManagement from './components/ChannelsManagement';
import Detections from './components/Detections';
import SettingsPage from './components/SettingsPage';

function App() {
  return (
    <ErrorBoundary>
      <Router>
        <div className="flex h-screen bg-gray-100">
          {/* Sidebar */}
          <nav className="w-64 bg-white shadow-lg">
            {/* ... (existing sidebar code) ... */}
          </nav>

          {/* Main content */}
          <main className="flex-1 p-8 overflow-y-auto">
            <Routes>
              <Route path="/" element={<HomeDashboard />} />
              <Route path="/ads" element={<AdsManagement />} />
              <Route path="/channels" element={<ChannelsManagement />} />
              <Route path="/detections" element={<Detections />} />
              <Route path="/settings" element={<SettingsPage />} />
            </Routes>
          </main>
        </div>
      </Router>
    </ErrorBoundary>
  );
}

export default App;