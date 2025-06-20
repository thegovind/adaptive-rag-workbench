import { BrowserRouter as Router, Routes, Route, Link, useLocation } from 'react-router-dom';
import { ContextAwareGeneration } from './pages/ContextAwareGeneration';
import { QAWithVerification } from './pages/QAWithVerification';
import { AdaptiveKBManagement } from './pages/AdaptiveKBManagement';
import { CitigroupLogo } from './components/CitigroupLogo';
import { GitHubLink } from './components/GitHubLink';
import { Card } from './components/ui/card';
import { Badge } from './components/ui/badge';
import { Brain, MessageSquare, Database } from 'lucide-react';
import './App.css';

function Navigation() {
  const location = useLocation();

  const isActive = (path: string) => location.pathname === path;

  const navItems = [
    {
      path: '/context-aware-generation',
      label: 'Context-Aware Generation',
      icon: Brain,
      description: 'AI-powered content generation',
      color: 'from-citigroup-blue to-citigroup-blue'
    },
    {
      path: '/qa-verification',
      label: 'QA with Verification',
      icon: MessageSquare,
      description: 'Multi-source verification',
      color: 'from-citigroup-red to-citigroup-red'
    },
    {
      path: '/adaptive-kb-management',
      label: 'Adaptive KB Management',
      icon: Database,
      description: 'Knowledge base curation',
      color: 'from-citigroup-blue to-citigroup-red'
    }
  ];

  return (
    <nav className="bg-white border-b border-gray-200 shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Top header with logo and actions */}
        <div className="flex justify-between items-center h-20">
          <div className="flex items-center space-x-4">
            <div className="w-12 h-12 bg-gradient-to-br from-citigroup-blue to-citigroup-blue rounded-xl flex items-center justify-center shadow-lg">
              <span className="text-white font-bold text-lg">AR</span>
            </div>
            <div>
              <h1 className="text-2xl font-bold text-citigroup-blue">Adaptive RAG Workbench</h1>
              <Badge variant="secondary" className="bg-citigroup-blue/10 text-citigroup-blue text-xs font-medium">
                Solution Accelerator
              </Badge>
            </div>
          </div>
          
          <div className="flex items-center space-x-4">
            <GitHubLink />
            <CitigroupLogo />
          </div>
        </div>
        
        {/* Navigation cards */}
        <div className="pb-4">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
            {navItems.map((item) => {
              const Icon = item.icon;
              const active = isActive(item.path);
              
              return (
                <Link key={item.path} to={item.path} className="block">
                  <Card className={`p-4 transition-all duration-300 cursor-pointer border-2 group hover:shadow-lg hover:-translate-y-0.5 ${
                    active 
                      ? 'border-citigroup-blue bg-gradient-to-br from-citigroup-blue/5 to-citigroup-blue/10 shadow-md' 
                      : 'border-gray-200 hover:border-citigroup-blue/40 hover:bg-gray-50/50'
                  }`}>
                    <div className="flex items-center space-x-3">
                      <div className={`p-2.5 rounded-lg transition-all duration-300 ${
                        active 
                          ? `bg-gradient-to-br ${item.color} text-white shadow-md` 
                          : 'bg-gray-100 text-gray-600 group-hover:bg-citigroup-blue/10 group-hover:text-citigroup-blue'
                      }`}>
                        <Icon className="h-5 w-5" />
                      </div>
                      <div className="flex-1 min-w-0">
                        <h3 className={`font-semibold text-base mb-0.5 transition-colors ${
                          active ? 'text-citigroup-blue' : 'text-gray-900 group-hover:text-citigroup-blue'
                        }`}>
                          {item.label}
                        </h3>
                        <p className="text-xs text-gray-600">
                          {item.description}
                        </p>
                      </div>
                      <div className={`transition-all duration-300 ${
                        active ? 'opacity-100' : 'opacity-0 group-hover:opacity-100'
                      }`}>
                        <div className="w-2 h-2 bg-citigroup-blue rounded-full"></div>
                      </div>
                    </div>
                  </Card>
                </Link>
              );
            })}
          </div>
        </div>
      </div>
    </nav>
  );
}

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gradient-to-br from-gray-50 to-citigroup-blue/5">
        <Navigation />
        <Routes>
          <Route path="/context-aware-generation" element={<ContextAwareGeneration />} />
          <Route path="/qa-verification" element={<QAWithVerification />} />
          <Route path="/adaptive-kb-management" element={<AdaptiveKBManagement />} />
          <Route path="/" element={<ContextAwareGeneration />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
