export interface PriceAlert {
  id: number;
  user_id: number;
  coin_id: string;
  target_price: number;
  direction: "above" | "below";
  active: boolean;
  created_at: string;
}

export interface AlertsListResponse {
  results: PriceAlert[];
}

export interface CreateAlertRequest {
  coin_id: string;
  target_price: number;
  direction: "above" | "below";
}

export interface CreateAlertResponse extends PriceAlert {}

export interface UpdateAlertRequest {
  id: number;
  active: boolean;
}

export interface UpdateAlertResponse extends PriceAlert {}

export interface DeleteAlertResponse {
  success: boolean;
}
