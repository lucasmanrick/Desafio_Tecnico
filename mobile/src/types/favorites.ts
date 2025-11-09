export interface FavoriteCoin {
  id: number;
  coin_id: string;
  user_id: number;
  added_at: string;
}

export interface FavoritesListResponse {
  results: FavoriteCoin[];
}

export interface AddFavoriteRequest {
  coin_id: string;
}

export interface AddFavoriteResponse extends FavoriteCoin {}

export interface RemoveFavoriteResponse {
  success: boolean;
}
