export interface HealthCheckResponse {
  status: "ok" | "error";
  database: boolean;
  coingecko_api: boolean;
  timestamp: string;
}
