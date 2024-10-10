import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
});

export const getAds = () => api.get('/ads');
export const createAd = (adData: FormData) => api.post('/ads', adData, {
  headers: { 'Content-Type': 'multipart/form-data' }
});
export const updateAd = (id: number, adData: FormData) => api.put(`/ads/${id}`, adData, {
  headers: { 'Content-Type': 'multipart/form-data' }
});
export const deleteAd = (id: number) => api.delete(`/ads/${id}`);
export const getChannels = () => api.get('/channels');
export const createChannel = (channelData: any) => api.post('/channels', channelData);
export const updateChannel = (id: number, channelData: any) => api.put(`/channels/${id}`, channelData);
export const deleteChannel = (id: number) => api.delete(`/channels/${id}`);
export const getDetections = () => api.get('/detections');
export const getSettings = () => api.get('/settings');
export const updateSettings = (settingsData: any) => api.post('/settings', settingsData);