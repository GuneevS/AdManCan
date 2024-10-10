import React, { useState, useEffect } from 'react';
import { Search, Plus, Edit, Trash2, MoreVertical, X } from 'lucide-react';
import { getChannels, createChannel } from '../api';

interface Channel {
  id: number;
  name: string;
  mediaType: 'tv' | 'radio';
  status: 'active' | 'inactive';
  health: number;
  lastScanned: string;
  folderPath: string;
  feeds: { id: number; name: string; url: string }[];
}

const ChannelsManagement: React.FC = () => {
  const [channels, setChannels] = useState<Channel[]>([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedMediaType, setSelectedMediaType] = useState<'all' | 'tv' | 'radio'>('all');
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentChannel, setCurrentChannel] = useState<Channel | null>(null);

  useEffect(() => {
    fetchChannels();
  }, []);

  const fetchChannels = async () => {
    try {
      const response = await getChannels();
      setChannels(response.data);
    } catch (error) {
      console.error('Error fetching channels:', error);
    }
  };

  const filteredChannels = channels.filter(channel =>
    channel.name.toLowerCase().includes(searchTerm.toLowerCase()) &&
    (selectedMediaType === 'all' || channel.mediaType === selectedMediaType)
  );

  const handleAddChannel = () => {
    setCurrentChannel(null);
    setIsModalOpen(true);
  };

  const handleEditChannel = (id: number) => {
    const channelToEdit = channels.find(channel => channel.id === id);
    if (channelToEdit) {
      setCurrentChannel(channelToEdit);
      setIsModalOpen(true);
    }
  };

  const handleDeleteChannel = (id: number) => {
    if (window.confirm('Are you sure you want to delete this channel?')) {
      // Implement delete API call here
      setChannels(channels.filter(channel => channel.id !== id));
    }
  };

  const handleToggleStatus = (id: number) => {
    if (window.confirm('Are you sure you want to change the status of this channel?')) {
      // Implement status toggle API call here
      setChannels(channels.map(channel =>
        channel.id === id ? { ...channel, status: channel.status === 'active' ? 'inactive' : 'active' } : channel
      ));
    }
  };

  const handleSaveChannel = async (channel: Channel) => {
    try {
      if (channel.id) {
        // Implement update API call here
      } else {
        const response = await createChannel(channel);
        setChannels([...channels, response.data]);
      }
      setIsModalOpen(false);
    } catch (error) {
      console.error('Error saving channel:', error);
    }
  };

  // ... rest of the component code ...

};

export default ChannelsManagement;