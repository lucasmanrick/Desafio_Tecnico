export interface PortfolioItem {
  id: number;
  user_id: number;
  coin_id: string;
  amount: number;
  average_price: number;
  created_at: string;
}

export interface PortfolioListResponse {
  results: PortfolioItem[];
}

export interface AddPortfolioRequest {
  coin_id: string;
  amount: number;
  average_price: number;
}

export interface AddPortfolioResponse extends PortfolioItem {}

export interface UpdatePortfolioRequest {
  id: number;
  amount?: number;
  average_price?: number;
}

export interface UpdatePortfolioResponse extends PortfolioItem {}

export interface RemovePortfolioResponse {
  success: boolean;
}
