import api from './api';

export interface Prediction {
  class: string;
  confidence: number;
  rank: number;
  plant?: string;
  disease?: string;
  is_healthy?: boolean;
}

export interface Recommendations {
  description: string;
  traitement: string[];
  prevention: string[];
  urgence: 'critique' | 'haute' | 'moyenne' | 'faible' | 'aucune';
}

export interface AnalysisResult {
  predictions: Prediction[];
  top_prediction: Prediction;
  recommendations?: Recommendations;
  summary?: string;
}

export interface AnalysisLog {
  id: number;
  user: number;
  user_username: string;
  image: string;
  image_url: string;
  result: AnalysisResult;
  confidence: number;
  processing_time: number;
  created_at: string;
}

export const analysisService = {
  async uploadImage(imageFile: File): Promise<AnalysisLog> {
    const formData = new FormData();
    formData.append('image', imageFile);
    
    const response = await api.post('/analysis/upload/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  },

  async getAnalysisHistory(): Promise<AnalysisLog[]> {
    const response = await api.get('/analysis/history/');
    return response.data;
  },

  async getAnalysisDetail(analysisId: number): Promise<AnalysisLog> {
    const response = await api.get(`/analysis/${analysisId}/`);
    return response.data;
  }
};