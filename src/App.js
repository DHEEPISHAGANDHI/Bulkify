import React, { useState, useEffect } from 'react';
import { Mic, Star, Users, Clock, ShoppingCart, Home, Recycle, Package, Bell, Phone, Mail, MapPin, Facebook, Twitter, Instagram, Linkedin, Award, Shield, Truck, HeadphonesIcon } from 'lucide-react';

const BulkifyApp = () => {
  const [selectedLanguage, setSelectedLanguage] = useState('english');
  const [activeTab, setActiveTab] = useState('home');
  const [isRecording, setIsRecording] = useState(false);
  const [voiceInput, setVoiceInput] = useState('');
  const [joinedOrders, setJoinedOrders] = useState([]);

  // Multilingual content
  const translations = {
    english: {
      appName: 'Bulkify',
      tagline: 'Bulk Orders Made Simple',
      home: 'Home',
      wasteExchange: 'Waste Exchange',
      groupOrders: 'Group Orders',
      alerts: 'Alerts',
      suppliers: 'Trusted Suppliers',
      joinGroupOrder: 'Join Group Order',
      voiceOrder: 'Voice Order',
      trustScore: 'Trust Score',
      pricePerUnit: 'Price per unit',
      startRecording: 'Start Voice Order',
      stopRecording: 'Stop Recording',
      groupProgress: 'Group Order Progress',
      vendorsJoined: 'vendors joined',
      timeLeft: 'Time left',
      buyNow: 'Buy Now',
      freshness: 'Freshness',
      quantity: 'Quantity',
      leftoverMaterials: 'Available Leftover Materials',
      myOrders: 'My Group Orders',
      activeOrders: 'Active Orders',
      completedOrders: 'Completed Orders',
      notifications: 'Notifications',
      priceAlerts: 'Price Alerts',
      footer: {
        about: 'About Bulkify',
        aboutText: 'Connecting retailers with bulk suppliers for better prices and reduced waste.',
        quickLinks: 'Quick Links',
        contact: 'Contact Us',
        followUs: 'Follow Us',
        rights: '© 2025 Bulkify. All rights reserved.'
      }
    },
    hindi: {
      appName: 'बल्किफाई',
      tagline: 'थोक ऑर्डर आसान बनाए',
      home: 'होम',
      wasteExchange: 'वेस्ट एक्सचेंज',
      groupOrders: 'ग्रुप ऑर्डर',
      alerts: 'अलर्ट',
      suppliers: 'विश्वसनीय आपूर्तिकर्ता',
      joinGroupOrder: 'ग्रुप ऑर्डर में शामिल हों',
      voiceOrder: 'वॉयस ऑर्डर',
      trustScore: 'ट्रस्ट स्कोर',
      pricePerUnit: 'प्रति यूनिट कीमत',
      startRecording: 'वॉयस ऑर्डर शुरू करें',
      stopRecording: 'रिकॉर्डिंग बंद करें',
      groupProgress: 'ग्रुप ऑर्डर प्रगति',
      vendorsJoined: 'विक्रेता शामिल हुए',
      timeLeft: 'समय बचा है',
      buyNow: 'अभी खरीदें',
      freshness: 'ताजगी',
      quantity: 'मात्रा',
      leftoverMaterials: 'उपलब्ध बचे हुए सामान',
      myOrders: 'मेरे ग्रुप ऑर्डर',
      activeOrders: 'सक्रिय ऑर्डर',
      completedOrders: 'पूर्ण ऑर्डर',
      notifications: 'सूचनाएं',
      priceAlerts: 'कीमत अलर्ट',
      footer: {
        about: 'बल्किफाई के बारे में',
        aboutText: 'बेहतर कीमतों और कम बर्बादी के लिए खुदरा विक्रेताओं को थोक आपूर्तिकर्ताओं से जोड़ना।',
        quickLinks: 'त्वरित लिंक',
        contact: 'संपर्क करें',
        followUs: 'फॉलो करें',
        rights: '© 2025 बल्किफाई। सभी अधिकार सुरक्षित।'
      }
    },
    tamil: {
      appName: 'பல்கிஃபை',
      tagline: 'மொத்த ஆர்டர்கள் எளிதாக்கப்பட்டது',
      home: 'முகப்பு',
      wasteExchange: 'கழிவு பரிமாற்றம்',
      groupOrders: 'குழு ஆர்டர்கள்',
      alerts: 'எச்சரிக்கைகள்',
      suppliers: 'நம்பகமான சப்ளையர்கள்',
      joinGroupOrder: 'குழு ஆர்டரில் சேரவும்',
      voiceOrder: 'குரல் ஆர்டர்',
      trustScore: 'நம்பகத்தன்மை மதிப்பெண்',
      pricePerUnit: 'ஒரு யூனிட் விலை',
      startRecording: 'குரல் ஆர்டர் தொடங்கவும்',
      stopRecording: 'பதிவை நிறுத்தவும்',
      groupProgress: 'குழு ஆர்டர் முன்னேற்றம்',
      vendorsJoined: 'விற்பனையாளர்கள் சேர்ந்தனர்',
      timeLeft: 'மீதமுள்ள நேரம்',
      buyNow: 'இப்போது வாங்கவும்',
      freshness: 'புத்துணர்வு',
      quantity: 'அளவு',
      leftoverMaterials: 'கிடைக்கும் மீதமுள்ள பொருட்கள்',
      myOrders: 'எனது குழு ஆர்டர்கள்',
      activeOrders: 'செயலில் உள்ள ஆர்டர்கள்',
      completedOrders: 'முடிந்த ஆர்டர்கள்',
      notifications: 'அறிவிப்புகள்',
      priceAlerts: 'விலை எச்சரிக்கைகள்',
      footer: {
        about: 'பல்கிஃபை பற்றி',
        aboutText: 'சிறந்த விலைகளுக்காகவும் கழிவுகளைக் குறைப்பதற்காகவும் சில்லறை விற்பனையாளர்களை மொத்த விற்பனையாளர்களுடன் இணைக்கிறது।',
        quickLinks: 'விரைவு இணைப்புகள்',
        contact: 'எங்களைத் தொடர்பு கொள்ளுங்கள்',
        followUs: 'எங்களை பின்தொடருங்கள்',
        rights: '© 2025 பல்கிஃபை. அனைத்து உரிமைகளும் பாதுகாக்கப்பட்டவை.'
      }
    },
    telugu: {
      appName: 'బల్కిఫై',
      tagline: 'మొత్తం ఆర్డర్లు సులభంగా చేయబడ్డాయి',
      home: 'హోమ్',
      wasteExchange: 'వేస్ట్ ఎక్స్‌చేంజ్',
      groupOrders: 'గ్రూప్ ఆర్డర్స్',
      alerts: 'అలర్ట్స్',
      suppliers: 'నమ్మకమైన సప్లైయర్లు',
      joinGroupOrder: 'గ్రూప్ ఆర్డర్‌లో చేరండి',
      voiceOrder: 'వాయిస్ ఆర్డర్',
      trustScore: 'ట్రస్ట్ స్కోర్',
      pricePerUnit: 'యూనిట్‌కు ధర',
      startRecording: 'వాయిస్ ఆర్డర్ ప్రారంభించండి',
      stopRecording: 'రికార్డింగ్ ఆపండి',
      groupProgress: 'గ్రూప్ ఆర్డర్ పురోగతి',
      vendorsJoined: 'వ్యాపారులు చేరారు',
      timeLeft: 'మిగిలిన సమయం',
      buyNow: 'ఇప్పుడు కొనండి',
      freshness: 'తాజాదనం',
      quantity: 'పరిమాణం',
      leftoverMaterials: 'అందుబాటులో ఉన్న మిగిలిన వస్తువులు',
      myOrders: 'నా గ్రూప్ ఆర్డర్లు',
      activeOrders: 'క్రియాశీల ఆర్డర్లు',
      completedOrders: 'పూర్తైన ఆర్డర్లు',
      notifications: 'నోటిఫికేషన్లు',
      priceAlerts: 'ధర హెచ్చరికలు',
      footer: {
        about: 'బల్కిఫై గురించి',
        aboutText: 'మెరుగైన ధరలు మరియు తక్కువ వ్యర్థాల కోసం రిటైలర్లను బల్క్ సప్లైయర్లతో కనెక్ట్ చేస్తోంది.',
        quickLinks: 'శీఘ్ర లింక్‌లు',
        contact: 'మమ్మల్ని సంప్రదించండి',
        followUs: 'మమ్మల్ని అనుసరించండి',
        rights: '© 2025 బల్కిఫై. అన్ని హక్కులు రిజర్వ్ చేయబడ్డాయి.'
      }
    }
  };

  const t = translations[selectedLanguage];

  // Expanded sample data
  const suppliers = [
    {
      id: 1,
      name: 'Raman Vegetables',
      product: 'Fresh Onions',
      image: '🧅',
      pricePerUnit: '₹25/kg',
      trustScore: 4.5,
      groupTarget: { current: 60, target: 100, unit: 'kg' },
      timeLeft: '2h 15m',
      location: 'Chennai',
      orders: 150
    },
    {
      id: 2,
      name: 'Krishna Spices',
      product: 'Red Chili Powder',
      image: '🌶️',
      pricePerUnit: '₹120/kg',
      trustScore: 4.8,
      groupTarget: { current: 25, target: 50, unit: 'kg' },
      timeLeft: '4h 30m',
      location: 'Madurai',
      orders: 200
    },
    {
      id: 3,
      name: 'Lakshmi Rice Mills',
      product: 'Basmati Rice',
      image: '🍚',
      pricePerUnit: '₹80/kg',
      trustScore: 4.2,
      groupTarget: { current: 150, target: 200, unit: 'kg' },
      timeLeft: '1h 45m',
      location: 'Coimbatore',
      orders: 300
    },
    {
      id: 4,
      name: 'Muthu Oils',
      product: 'Coconut Oil',
      image: '🥥',
      pricePerUnit: '₹180/L',
      trustScore: 4.6,
      groupTarget: { current: 40, target: 60, unit: 'L' },
      timeLeft: '3h 20m',
      location: 'Salem',
      orders: 120
    },
    {
      id: 5,
      name: 'Tamil Turmeric Co.',
      product: 'Organic Turmeric',
      image: '🧄',
      pricePerUnit: '₹200/kg',
      trustScore: 4.9,
      groupTarget: { current: 30, target: 40, unit: 'kg' },
      timeLeft: '5h 10m',
      location: 'Erode',
      orders: 180
    },
    {
      id: 6,
      name: 'Kaveri Grains',
      product: 'Black Gram Dal',
      image: '🫘',
      pricePerUnit: '₹150/kg',
      trustScore: 4.3,
      groupTarget: { current: 80, target: 120, unit: 'kg' },
      timeLeft: '6h 45m',
      location: 'Trichy',
      orders: 95
    }
  ];

  const wasteItems = [
    {
      id: 1,
      product: 'Tomatoes',
      image: '🍅',
      quantity: '15kg',
      freshness: 'Good',
      price: '₹15/kg',
      vendor: 'Suresh Vegetables',
      originalPrice: '₹30/kg',
      expiryTime: '6 hours',
      location: 'Chennai'
    },
    {
      id: 2,
      product: 'Potatoes',
      image: '🥔',
      quantity: '25kg',
      freshness: 'Excellent',
      price: '₹18/kg',
      vendor: 'Ganesh Farm',
      originalPrice: '₹35/kg',
      expiryTime: '12 hours',
      location: 'Vellore'
    },
    {
      id: 3,
      product: 'Carrots',
      image: '🥕',
      quantity: '10kg',
      freshness: 'Fair',
      price: '₹20/kg',
      vendor: 'Meera Store',
      originalPrice: '₹40/kg',
      expiryTime: '4 hours',
      location: 'Madurai'
    },
    {
      id: 4,
      product: 'Green Beans',
      image: '🫛',
      quantity: '8kg',
      freshness: 'Good',
      price: '₹25/kg',
      vendor: 'Ravi Vegetables',
      originalPrice: '₹50/kg',
      expiryTime: '8 hours',
      location: 'Coimbatore'
    },
    {
      id: 5,
      product: 'Cauliflower',
      image: '🥬',
      quantity: '12kg',
      freshness: 'Excellent',
      price: '₹22/kg',
      vendor: 'Prema Fresh',
      originalPrice: '₹45/kg',
      expiryTime: '10 hours',
      location: 'Salem'
    },
    {
      id: 6,
      product: 'Bell Peppers',
      image: '🫑',
      quantity: '6kg',
      freshness: 'Good',
      price: '₹35/kg',
      vendor: 'Organic Farm',
      originalPrice: '₹70/kg',
      expiryTime: '5 hours',
      location: 'Ooty'
    }
  ];

  const myGroupOrders = [
    {
      id: 1,
      product: 'Fresh Onions',
      supplier: 'Raman Vegetables',
      quantity: '5kg',
      status: 'Active',
      progress: 75,
      estimatedDelivery: '2 days',
      totalSavings: '₹50'
    },
    {
      id: 2,
      product: 'Basmati Rice',
      supplier: 'Lakshmi Rice Mills',
      quantity: '10kg',
      status: 'Completed',
      progress: 100,
      deliveredOn: 'Yesterday',
      totalSavings: '₹120'
    },
    {
      id: 3,
      product: 'Coconut Oil',
      supplier: 'Muthu Oils',
      quantity: '2L',
      status: 'Active',
      progress: 45,
      estimatedDelivery: '3 days',
      totalSavings: '₹30'
    }
  ];

  const notifications = [
    {
      id: 1,
      type: 'price_drop',
      title: 'Price Drop Alert!',
      message: 'Coconut Oil price dropped by 15% - Now ₹180/L',
      time: '2 hours ago',
      icon: '💰'
    },
    {
      id: 2,
      type: 'group_complete',
      title: 'Group Order Complete',
      message: 'Your Basmati Rice order is ready for delivery',
      time: '5 hours ago',
      icon: '✅'
    },
    {
      id: 3,
      type: 'new_supplier',
      title: 'New Supplier Added',
      message: 'Tamil Turmeric Co. joined with organic turmeric',
      time: '1 day ago',
      icon: '🆕'
    },
    {
      id: 4,
      type: 'waste_alert',
      title: 'Fresh Waste Available',
      message: 'Premium tomatoes available at 50% off',
      time: '3 hours ago',
      icon: '♻️'
    }
  ];

  const renderStars = (rating) => {
    return Array.from({ length: 5 }, (_, i) => (
      <Star
        key={i}
        size={16}
        className={i < Math.floor(rating) ? 'star-filled' : 'star-empty'}
        fill={i < Math.floor(rating) ? '#FFD700' : 'none'}
        stroke={i < Math.floor(rating) ? '#FFD700' : '#ccc'}
      />
    ));
  };

  const handleVoiceOrder = () => {
    setIsRecording(!isRecording);
    if (!isRecording) {
      setTimeout(() => {
        setVoiceInput('Order 10kg onions from Raman Vegetables');
        setIsRecording(false);
      }, 3000);
    }
  };

  const joinGroupOrder = (supplierId) => {
    if (!joinedOrders.includes(supplierId)) {
      setJoinedOrders([...joinedOrders, supplierId]);
    }
  };

  const renderVendorAvatars = (count) => {
    return Array.from({ length: Math.min(count, 6) }, (_, i) => (
      <div key={i} className="vendor-avatar">
        <Users size={16} />
      </div>
    ));
  };

  return (
    <div className="app">
      <style>{`
        * {
          margin: 0;
          padding: 0;
          box-sizing: border-box;
        }

        body {
          font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
          background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }

        .app {
          max-width: 1400px;
          margin: 0 auto;
          background: white;
          min-height: 100vh;
          box-shadow: 0 0 50px rgba(0,0,0,0.1);
          display: flex;
          flex-direction: column;
        }

        .header {
          background: linear-gradient(135deg, #2196F3, #21CBF3);
          color: white;
          padding: 2rem 3rem;
          display: flex;
          justify-content: space-between;
          align-items: center;
          box-shadow: 0 4px 20px rgba(0,0,0,0.15);
          position: relative;
          overflow: hidden;
        }

        .header::before {
          content: '';
          position: absolute;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background: radial-gradient(circle at 30% 70%, rgba(255,255,255,0.1) 0%, transparent 50%);
          pointer-events: none;
        }

        .logo-section {
          position: relative;
          z-index: 2;
        }

        .logo {
          font-size: 3rem;
          font-weight: 900;
          display: flex;
          align-items: center;
          gap: 1rem;
          margin-bottom: 0.5rem;
          text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
          letter-spacing: -1px;
        }

        .tagline {
          font-size: 1.2rem;
          opacity: 0.9;
          font-weight: 300;
          letter-spacing: 1px;
        }

        .language-selector {
          background: rgba(255,255,255,0.2);
          border: 2px solid rgba(255,255,255,0.3);
          color: white;
          padding: 1rem 1.5rem;
          border-radius: 30px;
          cursor: pointer;
          font-size: 1rem;
          font-weight: 500;
          backdrop-filter: blur(15px);
          transition: all 0.3s ease;
          position: relative;
          z-index: 2;
        }

        .language-selector:hover {
          background: rgba(255,255,255,0.3);
          transform: translateY(-2px);
        }

        .language-selector option {
          background: #2196F3;
          color: white;
          padding: 0.5rem;
        }

        .nav-bar {
          background: white;
          border-bottom: 3px solid #f0f0f0;
          padding: 0;
          display: flex;
          box-shadow: 0 3px 10px rgba(0,0,0,0.08);
          position: sticky;
          top: 0;
          z-index: 100;
        }

        .nav-tab {
          flex: 1;
          padding: 1.5rem 2rem;
          text-align: center;
          background: none;
          border: none;
          cursor: pointer;
          font-size: 1rem;
          font-weight: 600;
          color: #666;
          transition: all 0.3s ease;
          display: flex;
          align-items: center;
          justify-content: center;
          gap: 0.75rem;
          border-bottom: 4px solid transparent;
          position: relative;
        }

        .nav-tab::before {
          content: '';
          position: absolute;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background: linear-gradient(135deg, rgba(33, 150, 243, 0.05), rgba(33, 203, 243, 0.05));
          opacity: 0;
          transition: opacity 0.3s ease;
        }

        .nav-tab.active {
          color: #2196F3;
          border-bottom-color: #2196F3;
        }

        .nav-tab.active::before {
          opacity: 1;
        }

        .nav-tab:hover {
          color: #2196F3;
          transform: translateY(-2px);
        }

        .nav-tab:hover::before {
          opacity: 0.5;
        }

        .main-content {
          flex: 1;
          padding: 3rem;
          background: #f8f9fa;
        }

        .section-title {
          font-size: 2rem;
          font-weight: 700;
          margin-bottom: 2rem;
          color: #333;
          display: flex;
          align-items: center;
          gap: 1rem;
          position: relative;
        }

        .section-title::after {
          content: '';
          flex: 1;
          height: 3px;
          background: linear-gradient(90deg, #2196F3, transparent);
          border-radius: 2px;
        }

        .suppliers-grid, .waste-grid, .orders-grid {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
          gap: 2rem;
          margin-bottom: 3rem;
        }

        .supplier-card, .waste-card, .order-card {
          background: white;
          border-radius: 20px;
          padding: 2rem;
          box-shadow: 0 8px 25px rgba(0,0,0,0.1);
          transition: all 0.4s ease;
          border: 2px solid transparent;
          position: relative;
          overflow: hidden;
        }

        .supplier-card::before, .waste-card::before, .order-card::before {
          content: '';
          position: absolute;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background: linear-gradient(135deg, rgba(33, 150, 243, 0.02), rgba(33, 203, 243, 0.02));
          opacity: 0;
          transition: opacity 0.3s ease;
        }

        .supplier-card:hover, .waste-card:hover, .order-card:hover {
          transform: translateY(-8px);
          box-shadow: 0 15px 35px rgba(0,0,0,0.15);
          border-color: rgba(33, 150, 243, 0.2);
        }

        .supplier-card:hover::before, .waste-card:hover::before, .order-card:hover::before {
          opacity: 1;
        }

        .product-header, .waste-header, .order-header {
          display: flex;
          align-items: center;
          gap: 1.5rem;
          margin-bottom: 1.5rem;
          position: relative;
          z-index: 2;
        }

        .product-image, .waste-image {
          font-size: 4rem;
          background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
          border-radius: 20px;
          width: 100px;
          height: 100px;
          display: flex;
          align-items: center;
          justify-content: center;
          box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .waste-image {
          width: 80px;
          height: 80px;
          background: linear-gradient(135deg, #84fab0 0%, #8fd3f4 100%);
        }

        .product-info h3 {
          font-size: 1.4rem;
          color: #333;
          margin-bottom: 0.5rem;
          font-weight: 600;
        }

        .supplier-name {
          color: #666;
          font-size: 1rem;
          margin-bottom: 0.25rem;
        }

        .supplier-location {
          color: #999;
          font-size: 0.9rem;
          display: flex;
          align-items: center;
          gap: 0.25rem;
        }

        .product-details, .waste-details {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 1.5rem;
          position: relative;
          z-index: 2;
        }

        .price {
          font-size: 1.3rem;
          font-weight: bold;
          color: #28a745;
        }

        .original-price {
          font-size: 1rem;
          color: #999;
          text-decoration: line-through;
          margin-left: 0.5rem;
        }

        .trust-score {
          display: flex;
          align-items: center;
          gap: 0.75rem;
        }

        .trust-rating {
          display: flex;
          gap: 3px;
        }

        .star-filled, .star-empty {
          transition: all 0.2s ease;
        }

        .group-progress {
          background: #f8f9fa;
          padding: 1.5rem;
          border-radius: 15px;
          margin-bottom: 1.5rem;
          position: relative;
          z-index: 2;
        }

        .progress-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 1rem;
        }

        .progress-bar {
          height: 10px;
          background: #e9ecef;
          border-radius: 5px;
          overflow: hidden;
          margin-bottom: 1rem;
        }

        .progress-fill {
          height: 100%;
          background: linear-gradient(90deg, #28a745, #20c997);
          transition: width 0.3s ease;
        }

        .vendor-avatars {
          display: flex;
          gap: 0.5rem;
          margin-bottom: 1rem;
        }

        .vendor-avatar {
          width: 30px;
          height: 30px;
          background: linear-gradient(135deg, #667eea, #764ba2);
          border-radius: 50%;
          display: flex;
          align-items: center;
          justify-content: center;
          color: white;
        }

        .time-left {
          display: flex;
          align-items: center;
          gap: 0.5rem;
          color: #dc3545;
          font-size: 0.9rem;
          font-weight: 500;
        }

        .action-buttons {
          display: flex;
          gap: 1rem;
          position: relative;
          z-index: 2;
        }

        .btn {
          padding: 1rem 2rem;
          border: none;
          border-radius: 30px;
          cursor: pointer;
          font-weight: 600;
          transition: all 0.3s ease;
          display: flex;
          align-items: center;
          gap: 0.75rem;
          font-size: 1rem;
        }

        .btn-primary {
          background: linear-gradient(135deg, #2196F3, #21CBF3);
          color: white;
          flex: 1;
        }

        .btn-primary:hover {
          transform: translateY(-3px);
          box-shadow: 0 8px 20px rgba(33, 150, 243, 0.4);
        }

        .btn-primary.joined {
          background: linear-gradient(135deg, #28a745, #20c997);
        }

        .btn-secondary {
          background: rgba(33, 150, 243, 0.1);
          color: #2196F3;
          border: 2px solid rgba(33, 150, 243, 0.3);
          width: 60px;
          height: 60px;
          border-radius: 50%;
          justify-content: center;
          padding: 0;
        }

        .btn-secondary:hover {
          background: rgba(33, 150, 243, 0.2);
          transform: scale(1.1);
        }

        .voice-order-component {
          background: white;
          border-radius: 20px;
          padding: 2rem;
          margin-bottom: 3rem;
          box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        }

        .voice-controls {
          display: flex;
          align-items: center;
          gap: 1.5rem;
          margin-bottom: 1.5rem;
        }

        .voice-btn {
          width: 80px;
          height: 80px;
          border-radius: 50%;
          border: none;
          background: linear-gradient(135deg, #e74c3c, #c0392b);
          color: white;
          cursor: pointer;
          display: flex;
          align-items: center;
          justify-content: center;
          transition: all 0.3s ease;
        }

        .voice-btn.recording {
          background: linear-gradient(135deg, #28a745, #20c997);
          animation: pulse 1.5s infinite;
        }

        @keyframes pulse {
          0% { transform: scale(1); }
          50% { transform: scale(1.1); }
          100% { transform: scale(1); }
        }

        .voice-btn:hover {
          transform: scale(1.1);
        }

        .voice-status {
          flex: 1;
        }

        .voice-status h3 {
          font-size: 1.2rem;
          margin-bottom: 0.5rem;
          color: #333;
        }

        .voice-input {
          background: #f8f9fa;
          padding: 1.5rem;
          border-radius: 15px;
          border: 2px solid #e9ecef;
          font-style: italic;
          color: #666;
          min-height: 60px;
          display: flex;
          align-items: center;
          font-size: 1rem;
        }

        .freshness-badge {
          padding: 0.5rem 1rem;
          border-radius: 20px;
          font-size: 0.85rem;
          font-weight: 600;
        }

        .freshness-excellent {
          background: #d4edda;
          color: #155724;
        }

        .freshness-good {
          background: #fff3cd;
          color: #856404;
        }

        .freshness-fair {
          background: #f8d7da;
          color: #721c24;
        }

        .order-status {
          padding: 0.5rem 1rem;
          border-radius: 20px;
          font-size: 0.85rem;
          font-weight: 600;
          margin-bottom: 1rem;
        }

        .status-active {
          background: #d1ecf1;
          color: #0c5460;
        }

        .status-completed {
          background: #d4edda;
          color: #155724;
        }

        .notification-card {
          background: white;
          border-radius: 15px;
          padding: 1.5rem;
          margin-bottom: 1rem;
          box-shadow: 0 4px 15px rgba(0,0,0,0.08);
          border-left: 4px solid #2196F3;
          transition: all 0.3s ease;
        }

        .notification-card:hover {
          transform: translateX(5px);
          box-shadow: 0 6px 20px rgba(0,0,0,0.12);
        }

        .notification-header {
          display: flex;
          align-items: center;
          gap: 1rem;
          margin-bottom: 0.5rem;
        }

        .notification-icon {
          font-size: 1.5rem;
        }

        .notification-time {
          color: #999;
          font-size: 0.85rem;
          margin-top: 0.5rem;
        }

        .empty-state {
          text-align: center;
          padding: 4rem 2rem;
          color: #666;
        }

        .empty-state-icon {
          margin-bottom: 1.5rem;
          opacity: 0.5;
        }

        .empty-state h3 {
          font-size: 1.5rem;
          margin-bottom: 1rem;
        }

        .footer {
          background: linear-gradient(135deg, #2c3e50, #34495e);
          color: white;
          padding: 4rem 3rem 2rem;
          margin-top: auto;
        }

        .footer-content {
          display: grid;
          grid-template-columns: 2fr 1fr 1fr 1fr;
          gap: 3rem;
          margin-bottom: 2rem;
        }

        .footer-section h3 {
          font-size: 1.3rem;
          margin-bottom: 1.5rem;
          color: #ecf0f1;
        }

        .footer-section p {
          line-height: 1.6;
          color: #bdc3c7;
          margin-bottom: 1rem;
        }

        .footer-links {
          list-style: none;
        }

        .footer-links li {
          margin-bottom: 0.75rem;
        }

        .footer-links a {
          color: #bdc3c7;
          text-decoration: none;
          transition: color 0.3s ease;
        }

        .footer-links a:hover {
          color: #3498db;
        }

        .contact-info {
          display: flex;
          align-items: center;
          gap: 0.75rem;
          margin-bottom: 1rem;
          color: #bdc3c7;
        }

        .social-links {
          display: flex;
          gap: 1rem;
          margin-top: 1rem;
        }

        .social-link {
          width: 40px;
          height: 40px;
          border-radius: 50%;
          background: rgba(255,255,255,0.1);
          display: flex;
          align-items: center;
          justify-content: center;
          color: #bdc3c7;
          transition: all 0.3s ease;
        }

        .social-link:hover {
          background: #3498db;
          color: white;
          transform: translateY(-3px);
        }

        .footer-bottom {
          border-top: 1px solid rgba(255,255,255,0.1);
          padding-top: 2rem;
          text-align: center;
          color: #95a5a6;
        }

        @media (max-width: 1200px) {
          .suppliers-grid, .waste-grid, .orders-grid {
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
          }
        }

        @media (max-width: 768px) {
          .header {
            flex-direction: column;
            gap: 1.5rem;
            text-align: center;
            padding: 1.5rem;
          }
          
          .logo {
            font-size: 2rem;
          }
          
          .nav-tab {
            font-size: 0.9rem;
            padding: 1rem 0.5rem;
          }
          
          .main-content {
            padding: 1.5rem;
          }
          
          .suppliers-grid, .waste-grid, .orders-grid {
            grid-template-columns: 1fr;
          }
          
          .footer-content {
            grid-template-columns: 1fr;
            gap: 2rem;
          }
        }
      `}</style>

      <header className="header">
        <div className="logo-section">
          <div className="logo">
            <Package size={48} />
            {t.appName}
          </div>
          <div className="tagline">{t.tagline}</div>
        </div>
        <select 
          className="language-selector"
          value={selectedLanguage}
          onChange={(e) => setSelectedLanguage(e.target.value)}
        >
          <option value="english">English</option>
          <option value="hindi">हिंदी</option>
          <option value="tamil">தமிழ்</option>
          <option value="telugu">తెలుగు</option>
        </select>
      </header>

      <nav className="nav-bar">
        <button 
          className={`nav-tab ${activeTab === 'home' ? 'active' : ''}`}
          onClick={() => setActiveTab('home')}
        >
          <Home size={20} />
          {t.home}
        </button>
        <button 
          className={`nav-tab ${activeTab === 'waste' ? 'active' : ''}`}
          onClick={() => setActiveTab('waste')}
        >
          <Recycle size={20} />
          {t.wasteExchange}
        </button>
        <button 
          className={`nav-tab ${activeTab === 'orders' ? 'active' : ''}`}
          onClick={() => setActiveTab('orders')}
        >
          <Package size={20} />
          {t.groupOrders}
        </button>
        <button 
          className={`nav-tab ${activeTab === 'alerts' ? 'active' : ''}`}
          onClick={() => setActiveTab('alerts')}
        >
          <Bell size={20} />
          {t.alerts}
        </button>
      </nav>

      <main className="main-content">
        {activeTab === 'home' && (
          <>
            <div className="voice-order-component">
              <h2 className="section-title">
                <Mic size={24} />
                {t.voiceOrder}
              </h2>
              <div className="voice-controls">
                <button 
                  className={`voice-btn ${isRecording ? 'recording' : ''}`}
                  onClick={handleVoiceOrder}
                >
                  <Mic size={32} />
                </button>
                <div className="voice-status">
                  <h3>{isRecording ? t.stopRecording : t.startRecording}</h3>
                  <p>Speak clearly to place your order</p>
                </div>
              </div>
              <div className="voice-input">
                {voiceInput || (isRecording ? 'Listening...' : 'Tap the mic to start voice ordering')}
              </div>
            </div>

            <h2 className="section-title">
              <Users size={24} />
              {t.suppliers}
            </h2>
            <div className="suppliers-grid">
              {suppliers.map((supplier) => (
                <div key={supplier.id} className="supplier-card">
                  <div className="product-header">
                    <div className="product-image">{supplier.image}</div>
                    <div className="product-info">
                      <h3>{supplier.product}</h3>
                      <p className="supplier-name">{supplier.name}</p>
                      <div className="supplier-location">
                        <MapPin size={14} />
                        {supplier.location}
                      </div>
                    </div>
                  </div>
                  
                  <div className="product-details">
                    <div className="price">{supplier.pricePerUnit}</div>
                    <div className="trust-score">
                      <span>{t.trustScore}:</span>
                      <div className="trust-rating">
                        {renderStars(supplier.trustScore)}
                      </div>
                      <span style={{fontSize: '0.9rem', color: '#666'}}>({supplier.orders} orders)</span>
                    </div>
                  </div>

                  <div className="group-progress">
                    <div className="progress-header">
                      <span style={{fontWeight: '600'}}>{t.groupProgress}</span>
                      <div className="time-left">
                        <Clock size={16} />
                        {supplier.timeLeft} {t.timeLeft}
                      </div>
                    </div>
                    <div className="vendor-avatars">
                      {renderVendorAvatars(Math.floor(supplier.groupTarget.current / 10))}
                      <span style={{marginLeft: '0.75rem', fontSize: '0.9rem', color: '#666'}}>
                        {Math.floor(supplier.groupTarget.current / 10)} {t.vendorsJoined}
                      </span>
                    </div>
                    <div className="progress-bar">
                      <div 
                        className="progress-fill"
                        style={{width: `${(supplier.groupTarget.current / supplier.groupTarget.target) * 100}%`}}
                      ></div>
                    </div>
                    <p style={{fontSize: '1rem', color: '#666', marginTop: '0.75rem', fontWeight: '500'}}>
                      {supplier.groupTarget.current}{supplier.groupTarget.unit} / {supplier.groupTarget.target}{supplier.groupTarget.unit}
                    </p>
                  </div>

                  <div className="action-buttons">
                    <button 
                      className={`btn btn-primary ${joinedOrders.includes(supplier.id) ? 'joined' : ''}`}
                      onClick={() => joinGroupOrder(supplier.id)}
                    >
                      <ShoppingCart size={18} />
                      {joinedOrders.includes(supplier.id) ? 'Joined!' : t.joinGroupOrder}
                    </button>
                    <button className="btn btn-secondary">
                      <Mic size={20} />
                    </button>
                  </div>
                </div>
              ))}
            </div>
          </>
        )}

        {activeTab === 'waste' && (
          <>
            <h2 className="section-title">
              <Recycle size={24} />
              {t.leftoverMaterials}
            </h2>
            <div className="waste-grid">
              {wasteItems.map((item) => (
                <div key={item.id} className="waste-card">
                  <div className="waste-header">
                    <div className="waste-image">{item.image}</div>
                    <div style={{flex: 1}}>
                      <h3>{item.product}</h3>
                      <p className="supplier-name">{item.vendor}</p>
                      <div className="supplier-location">
                        <MapPin size={14} />
                        {item.location}
                      </div>
                    </div>
                    <span className={`freshness-badge freshness-${item.freshness.toLowerCase()}`}>
                      {t.freshness}: {item.freshness}
                    </span>
                  </div>
                  
                  <div className="waste-details">
                    <div>
                      <p style={{marginBottom: '0.5rem'}}><strong>{t.quantity}:</strong> {item.quantity}</p>
                      <p className="price">
                        {item.price}
                        <span className="original-price">{item.originalPrice}</span>
                      </p>
                    </div>
                    <div style={{textAlign: 'right'}}>
                      <div className="time-left">
                        <Clock size={14} />
                        {item.expiryTime} left
                      </div>
                    </div>
                  </div>

                  <button className="btn btn-primary" style={{width: '100%', marginTop: '1.5rem'}}>
                    <ShoppingCart size={18} />
                    {t.buyNow}
                  </button>
                </div>
              ))}
            </div>
          </>
        )}

        {activeTab === 'orders' && (
          <>
            <h2 className="section-title">
              <Package size={24} />
              {t.myOrders}
            </h2>
            <div className="orders-grid">
              {myGroupOrders.map((order) => (
                <div key={order.id} className="order-card">
                  <div className="order-header">
                    <div style={{flex: 1}}>
                      <h3>{order.product}</h3>
                      <p className="supplier-name">{order.supplier}</p>
                      <p style={{color: '#666', fontSize: '0.9rem'}}>Quantity: {order.quantity}</p>
                    </div>
                    <span className={`order-status status-${order.status.toLowerCase()}`}>
                      {order.status}
                    </span>
                  </div>

                  <div className="group-progress">
                    <div className="progress-header">
                      <span style={{fontWeight: '600'}}>Progress</span>
                      <span style={{fontSize: '0.9rem', color: '#666'}}>{order.progress}%</span>
                    </div>
                    <div className="progress-bar">
                      <div 
                        className="progress-fill"
                        style={{width: `${order.progress}%`}}
                      ></div>
                    </div>
                  </div>

                  <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '1rem'}}>
                    <div>
                      <p style={{color: '#666', fontSize: '0.9rem'}}>
                        {order.status === 'Completed' ? 'Delivered' : 'Estimated delivery'}
                      </p>
                      <p style={{fontWeight: '600'}}>
                        {order.status === 'Completed' ? order.deliveredOn : order.estimatedDelivery}
                      </p>
                    </div>
                    <div style={{textAlign: 'right'}}>
                      <p style={{color: '#666', fontSize: '0.9rem'}}>Total savings</p>
                      <p style={{fontWeight: '600', color: '#28a745'}}>{order.totalSavings}</p>
                    </div>
                  </div>

                  {order.status === 'Active' && (
                    <button className="btn btn-primary" style={{width: '100%', marginTop: '1rem'}}>
                      <Truck size={18} />
                      Track Order
                    </button>
                  )}
                </div>
              ))}
            </div>
          </>
        )}

        {activeTab === 'alerts' && (
          <>
            <h2 className="section-title">
              <Bell size={24} />
              {t.notifications}
            </h2>
            <div style={{maxWidth: '800px'}}>
              {notifications.map((notification) => (
                <div key={notification.id} className="notification-card">
                  <div className="notification-header">
                    <span className="notification-icon">{notification.icon}</span>
                    <div style={{flex: 1}}>
                      <h4 style={{margin: 0, fontSize: '1.1rem'}}>{notification.title}</h4>
                      <p style={{margin: '0.5rem 0 0', color: '#666'}}>{notification.message}</p>
                    </div>
                  </div>
                  <div className="notification-time">{notification.time}</div>
                </div>
              ))}
            </div>
          </>
        )}
      </main>

      <footer className="footer">
        <div className="footer-content">
          <div className="footer-section">
            <h3>{t.footer.about}</h3>
            <p>{t.footer.aboutText}</p>
            <div style={{display: 'flex', alignItems: 'center', gap: '1rem', marginTop: '1rem'}}>
              <Award size={20} color="#f39c12" />
              <span>Trusted by 10,000+ retailers</span>
            </div>
            <div style={{display: 'flex', alignItems: 'center', gap: '1rem', marginTop: '0.5rem'}}>
              <Shield size={20} color="#27ae60" />
              <span>100% Secure Transactions</span>
            </div>
          </div>

          <div className="footer-section">
            <h3>{t.footer.quickLinks}</h3>
            <ul className="footer-links">
              <li><a href="#home">{t.home}</a></li>
              <li><a href="#suppliers">{t.suppliers}</a></li>
              <li><a href="#waste">{t.wasteExchange}</a></li>
              <li><a href="#orders">{t.groupOrders}</a></li>
              <li><a href="#help">Help & Support</a></li>
            </ul>
          </div>

          <div className="footer-section">
            <h3>{t.footer.contact}</h3>
            <div className="contact-info">
              <Phone size={16} />
              <span>+91 98765 43210</span>
            </div>
            <div className="contact-info">
              <Mail size={16} />
              <span>support@bulkify.com</span>
            </div>
            <div className="contact-info">
              <MapPin size={16} />
              <span>Chennai, Tamil Nadu</span>
            </div>
            <div className="contact-info">
              <HeadphonesIcon size={16} />
              <span>24/7 Customer Support</span>
            </div>
          </div>

          <div className="footer-section">
            <h3>{t.footer.followUs}</h3>
            <div className="social-links">
              <a href="#" className="social-link">
                <Facebook size={20} />
              </a>
              <a href="#" className="social-link">
                <Twitter size={20} />
              </a>
              <a href="#" className="social-link">
                <Instagram size={20} />
              </a>
              <a href="#" className="social-link">
                <Linkedin size={20} />
              </a>
            </div>
          </div>
        </div>

        <div className="footer-bottom">
          <p>{t.footer.rights}</p>
        </div>
      </footer>
    </div>
  );
};

export default BulkifyApp;