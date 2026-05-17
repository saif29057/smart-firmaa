import React, { useState, useRef } from 'react';
import { analysisService, AnalysisLog, Prediction } from '../services/analysisService';
import '../styles/ModernAnalysis.css';

const Analysis: React.FC = () => {
  const [selectedImage, setSelectedImage] = useState<File | null>(null);
  const [previewUrl, setPreviewUrl] = useState<string>('');
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [result, setResult] = useState<AnalysisLog | null>(null);
  const [history, setHistory] = useState<AnalysisLog[]>([]);
  const [error, setError] = useState('');
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleImageSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      if (file.size > 10 * 1024 * 1024) {
        setError('L\'image ne doit pas dépasser 10MB');
        return;
      }

      if (!file.type.startsWith('image/')) {
        setError('Veuillez sélectionner une image valide');
        return;
      }

      setSelectedImage(file);
      setPreviewUrl(URL.createObjectURL(file));
      setError('');
      setResult(null);
    }
  };

  const handleAnalyze = async () => {
    if (!selectedImage) return;

    setIsAnalyzing(true);
    setError('');

    try {
      const analysisResult = await analysisService.uploadImage(selectedImage);
      setResult(analysisResult);
      
      // Ajouter à l'historique
      setHistory(prev => [analysisResult, ...prev]);
    } catch (err: any) {
      setError(err.response?.data?.error || 'Erreur lors de l\'analyse');
    } finally {
      setIsAnalyzing(false);
    }
  };

  const handleReset = () => {
    setSelectedImage(null);
    setPreviewUrl('');
    setResult(null);
    setError('');
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  const getConfidenceColor = (confidence: number) => {
    if (confidence >= 0.8) return '#27ae60';
    if (confidence >= 0.6) return '#f39c12';
    return '#e74c3c';
  };

  const formatTime = (seconds: number) => {
    return `${(seconds * 1000).toFixed(0)}ms`;
  };

  const getUrgenceConfig = (urgence: string) => {
    switch (urgence) {
      case 'critique':
        return { color: '#e74c3c', bg: '#fdf2f2', border: '#f5c6c6', icon: '🚨', label: 'CRITIQUE — Agir immédiatement' };
      case 'haute':
        return { color: '#e67e22', bg: '#fef9f0', border: '#fde8c8', icon: '⚠️', label: 'Urgence haute' };
      case 'moyenne':
        return { color: '#f39c12', bg: '#fffdf0', border: '#fdefc8', icon: '⚡', label: 'Urgence moyenne' };
      case 'faible':
        return { color: '#27ae60', bg: '#f0fdf4', border: '#bbf7d0', icon: '✅', label: 'Urgence faible' };
      case 'aucune':
        return { color: '#27ae60', bg: '#f0fdf4', border: '#bbf7d0', icon: '🌿', label: 'Plante saine' };
      default:
        return { color: '#6b7280', bg: '#f9fafb', border: '#e5e7eb', icon: 'ℹ️', label: 'À surveiller' };
    }
  };

  const RecommendationsBox: React.FC<{ recommendations: any }> = ({ recommendations }) => {
    if (!recommendations) return null;

    const urgenceConfig = getUrgenceConfig(recommendations.urgence);
    const isHealthy = recommendations.urgence === 'aucune';

    return (
      <div className="recommendations-card modern-card" style={{
        border: `2px solid ${urgenceConfig.border}`,
        borderRadius: '16px',
        overflow: 'hidden',
        marginTop: '20px',
        background: '#fff',
        boxShadow: '0 4px 20px rgba(0,0,0,0.08)',
      }}>
        {/* Header */}
        <div style={{
          background: urgenceConfig.bg,
          borderBottom: `1px solid ${urgenceConfig.border}`,
          padding: '18px 24px',
          display: 'flex',
          alignItems: 'center',
          gap: '12px',
        }}>
          <span style={{ fontSize: '28px' }}>{urgenceConfig.icon}</span>
          <div>
            <h3 style={{ margin: 0, color: urgenceConfig.color, fontSize: '1.1rem', fontWeight: 700 }}>
              Recommandations Agronomiques
            </h3>
            <span style={{
              display: 'inline-block',
              marginTop: '4px',
              padding: '2px 10px',
              borderRadius: '20px',
              fontSize: '0.75rem',
              fontWeight: 600,
              color: urgenceConfig.color,
              background: `${urgenceConfig.color}18`,
              border: `1px solid ${urgenceConfig.color}40`,
            }}>
              {urgenceConfig.label}
            </span>
          </div>
        </div>

        <div style={{ padding: '20px 24px', display: 'flex', flexDirection: 'column', gap: '20px' }}>
          {/* Description */}
          <div style={{
            padding: '14px 16px',
            background: urgenceConfig.bg,
            borderRadius: '10px',
            border: `1px solid ${urgenceConfig.border}`,
          }}>
            <p style={{ margin: 0, color: '#374151', lineHeight: 1.6, fontSize: '0.92rem' }}>
              {recommendations.description}
            </p>
          </div>

          {/* Traitement */}
          {recommendations.traitement && recommendations.traitement.length > 0 && (
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '12px' }}>
                <span style={{
                  width: '28px', height: '28px',
                  background: '#fee2e2',
                  borderRadius: '8px',
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  fontSize: '14px',
                }}>💊</span>
                <h4 style={{ margin: 0, color: '#1f2937', fontSize: '0.95rem', fontWeight: 700 }}>
                  Traitement recommandé
                </h4>
              </div>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                {recommendations.traitement.map((item: string, i: number) => (
                  <div key={i} style={{
                    display: 'flex',
                    alignItems: 'flex-start',
                    gap: '10px',
                    padding: '10px 14px',
                    background: '#fff5f5',
                    borderRadius: '8px',
                    border: '1px solid #fecaca',
                  }}>
                    <span style={{
                      flexShrink: 0,
                      width: '20px', height: '20px',
                      background: '#e74c3c',
                      color: '#fff',
                      borderRadius: '50%',
                      display: 'flex', alignItems: 'center', justifyContent: 'center',
                      fontSize: '11px',
                      fontWeight: 700,
                      marginTop: '1px',
                    }}>{i + 1}</span>
                    <span style={{ color: '#374151', fontSize: '0.88rem', lineHeight: 1.5 }}>{item}</span>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Prévention */}
          {recommendations.prevention && recommendations.prevention.length > 0 && (
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '12px' }}>
                <span style={{
                  width: '28px', height: '28px',
                  background: '#d1fae5',
                  borderRadius: '8px',
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  fontSize: '14px',
                }}>🛡️</span>
                <h4 style={{ margin: 0, color: '#1f2937', fontSize: '0.95rem', fontWeight: 700 }}>
                  {isHealthy ? 'Bonnes pratiques à maintenir' : 'Prévention future'}
                </h4>
              </div>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                {recommendations.prevention.map((item: string, i: number) => (
                  <div key={i} style={{
                    display: 'flex',
                    alignItems: 'flex-start',
                    gap: '10px',
                    padding: '10px 14px',
                    background: '#f0fdf4',
                    borderRadius: '8px',
                    border: '1px solid #bbf7d0',
                  }}>
                    <span style={{
                      flexShrink: 0,
                      color: '#27ae60',
                      fontSize: '16px',
                      marginTop: '1px',
                    }}>✓</span>
                    <span style={{ color: '#374151', fontSize: '0.88rem', lineHeight: 1.5 }}>{item}</span>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Footer conseil */}
          {!isHealthy && (
            <div style={{
              display: 'flex',
              alignItems: 'center',
              gap: '10px',
              padding: '12px 16px',
              background: '#f8fafc',
              borderRadius: '10px',
              border: '1px solid #e2e8f0',
            }}>
              <span style={{ fontSize: '18px' }}>👨‍🌾</span>
              <p style={{ margin: 0, color: '#64748b', fontSize: '0.82rem', lineHeight: 1.5 }}>
                <strong>Conseil :</strong> En cas de doute ou de maladie sévère, contactez un agronome local pour un diagnostic sur place.
              </p>
            </div>
          )}
        </div>
      </div>
    );
  };

  return (
    <div className="analysis-page">
      {/* Hero Section */}
      <div className="analysis-hero">
        <div className="hero-content">
          <div className="hero-icon">🌿</div>
          <h1>Analyse Agricole Intelligente</h1>
          <p className="hero-subtitle">Détectez les maladies des plantes avec notre IA spécialisée pour l'agriculture tunisienne</p>
          <div className="hero-stats">
            <div className="stat-item">
              <span className="stat-number">95%</span>
              <span className="stat-label">Précision</span>
            </div>
            <div className="stat-item">
              <span className="stat-number">50+</span>
              <span className="stat-label">Maladies</span>
            </div>
            <div className="stat-item">
              <span className="stat-number">{'<'}2s</span>
              <span className="stat-label">Analyse</span>
            </div>
          </div>
        </div>
        <div className="hero-decoration">
          <div className="leaf-pattern">🍃</div>
        </div>
      </div>

      <div className="analysis-content">
        <div className="upload-section">
          <div className="upload-card modern-card">
            <div className="card-header">
              <div className="card-icon">📸</div>
              <h2>Analyse de Plante</h2>
              <p>Prenez une photo ou téléchargez une image de votre plante</p>
            </div>
            
            <div className="upload-area modern-upload">
              {previewUrl ? (
                <div className="image-preview-container">
                  <div className="preview-wrapper">
                    <img src={previewUrl} alt="Preview" className="preview-image" />
                    <div className="preview-overlay">
                      <button onClick={handleReset} className="btn btn-outline change-btn">
                        <span className="btn-icon">🔄</span>
                        Changer
                      </button>
                    </div>
                  </div>
                </div>
              ) : (
                <div className="upload-placeholder modern-placeholder">
                  <div className="placeholder-content">
                    <div className="placeholder-icon">🌿</div>
                    <h3>Cliquez pour analyser</h3>
                    <p>Glissez-déposez une image ou cliquez pour sélectionner</p>
                    <div className="supported-formats">
                      <span className="format-tag">PNG</span>
                      <span className="format-tag">JPG</span>
                      <span className="format-tag">GIF</span>
                      <span className="size-info">Max 10MB</span>
                    </div>
                  </div>
                </div>
              )}
              
              <input
                ref={fileInputRef}
                type="file"
                accept="image/*"
                onChange={handleImageSelect}
                className="file-input"
              />
            </div>

            {error && <div className="alert alert-error modern-alert">{error}</div>}

            {selectedImage && (
              <div className="upload-actions">
                <button
                  onClick={handleAnalyze}
                  disabled={isAnalyzing}
                  className="btn btn-primary analyze-btn modern-analyze-btn"
                >
                  <span className="btn-icon">🔍</span>
                  {isAnalyzing ? 'Analyse en cours...' : 'Lancer l\'analyse IA'}
                </button>
              </div>
            )}
          </div>
        </div>

        {result && (
          <div className="results-section">
            <div className="results-card modern-results">
              <div className="results-header">
                <div className="results-icon">🌿</div>
                <h2>Résultats de l'Analyse IA</h2>
                <div className="confidence-badge" style={{ 
                  backgroundColor: getConfidenceColor(result.confidence),
                  color: '#fff'
                }}>
                  {(result.confidence * 100).toFixed(1)}% de confiance
                </div>
              </div>
              
              <div className="result-summary">
                <div className="top-prediction main-prediction">
                  <div className="prediction-header">
                    <h3>Diagnostic Principal</h3>
                    <div className="prediction-status">
                      <span className="status-dot" style={{ 
                        backgroundColor: getConfidenceColor(result.result.top_prediction.confidence)
                      }}></span>
                      {result.result.top_prediction.confidence >= 0.8 ? 'Haute confiance' : 
                       result.result.top_prediction.confidence >= 0.6 ? 'Confiance moyenne' : 'Faible confiance'}
                    </div>
                  </div>
                  <div className="prediction-item main">
                    <div className="disease-info">
                      <div className="disease-icon">🦠</div>
                      <div className="disease-details">
                        <span className="class-name">{result.result.top_prediction.class}</span>
                        <div className="confidence-visual">
                          <div className="confidence-progress">
                            <div 
                              className="confidence-fill"
                              style={{ 
                                width: `${result.result.top_prediction.confidence * 100}%`,
                                backgroundColor: getConfidenceColor(result.result.top_prediction.confidence)
                              }}
                            ></div>
                          </div>
                          <span className="confidence-percentage">
                            {(result.result.top_prediction.confidence * 100).toFixed(1)}%
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <div className="all-predictions predictions-list">
                  <h3>Autres possibilités</h3>
                  <div className="predictions-grid">
                    {result.result.predictions.slice(1).map((prediction: Prediction, index: number) => (
                      <div key={index} className="prediction-card">
                        <div className="prediction-rank">#{prediction.rank + 1}</div>
                        <div className="prediction-content">
                          <span className="class-name">{prediction.class}</span>
                          <div className="mini-confidence-bar">
                            <div 
                              className="confidence-fill"
                              style={{ 
                                width: `${prediction.confidence * 100}%`,
                                backgroundColor: getConfidenceColor(prediction.confidence)
                              }}
                            ></div>
                          </div>
                          <span className="confidence-value">
                            {(prediction.confidence * 100).toFixed(1)}%
                          </span>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </div>

              {/* ── Recommendations Box ── */}
              {result.result.recommendations && (
                <RecommendationsBox recommendations={result.result.recommendations} />
              )}

              <div className="analysis-meta modern-meta">
                <div className="meta-grid">
                  <div className="meta-item">
                    <div className="meta-icon">⚡</div>
                    <div className="meta-content">
                      <span className="label">Temps de traitement</span>
                      <span className="value">{formatTime(result.processing_time)}</span>
                    </div>
                  </div>
                  <div className="meta-item">
                    <div className="meta-icon">📅</div>
                    <div className="meta-content">
                      <span className="label">Date d'analyse</span>
                      <span className="value">
                        {new Date(result.created_at).toLocaleString('fr-FR')}
                      </span>
                    </div>
                  </div>
                  <div className="meta-item">
                    <div className="meta-icon">🎯</div>
                    <div className="meta-content">
                      <span className="label">Confiance globale</span>
                      <span className="value confidence-high">
                        {(result.confidence * 100).toFixed(1)}%
                      </span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {history.length > 0 && (
          <div className="history-section">
            <div className="history-header">
              <div className="history-icon">📊</div>
              <h2>Historique des Analyses</h2>
              <p>Vos analyses précédentes de maladies des plantes</p>
            </div>
            <div className="history-grid modern-history">
              {history.map((item) => (
                <div key={item.id} className="history-item modern-history-item">
                  <div className="history-image-container">
                    <img 
                      src={item.image_url} 
                      alt="Analysis" 
                      className="history-image"
                    />
                    <div className="history-overlay">
                      <div className="confidence-indicator" style={{ 
                        backgroundColor: getConfidenceColor(item.result.top_prediction?.confidence || 0)
                      }}>
                        {(item.result.top_prediction?.confidence || 0 * 100).toFixed(0)}%
                      </div>
                    </div>
                  </div>
                  <div className="history-info">
                    <div className="history-result">
                      <span className="result-label">Diagnostic:</span>
                      <span className="result-value">{item.result.top_prediction?.class}</span>
                    </div>
                    <div className="history-meta">
                      <div className="confidence-item">
                        <span className="meta-mini-icon">🎯</span>
                        {(item.result.top_prediction?.confidence || 0 * 100).toFixed(1)}%
                      </div>
                      <div className="date-item">
                        <span className="meta-mini-icon">📅</span>
                        {new Date(item.created_at).toLocaleDateString('fr-FR')}
                      </div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Analysis;