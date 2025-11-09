export interface Coin {
  id: string;
  symbol: string;
  name: string;
  image: string;
  current_price: number;
  price_change_24h: number;
  price_change_percentage_24h: number;
  market_cap: number;
  market_cap_rank: number;
  total_volume: number;
  high_24h: number;
  low_24h: number;
  cached: boolean;
  cached_at: string;
}

export interface CoinListResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: Coin[];
}

export interface CoinDetailResponse extends Coin {
  description: string;
  circulating_supply: number;
  total_supply: number;
  max_supply: number;
  ath: number;
  ath_date: string;
  links: {
    homepage: string;
    blockchain_site: string;
    official_forum: string;
  };
}

export interface CoinChartResponse {
  prices: [number, number][];
  cached: boolean;
  cached_at: string;
}
