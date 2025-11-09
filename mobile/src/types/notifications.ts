export interface Notification {
  id: number;
  user_id: number;
  title: string;
  message: string;
  read: boolean;
  created_at: string;
}

export interface NotificationsListResponse {
  results: Notification[];
}

export interface MarkAsReadRequest {
  id: number;
}

export interface MarkAsReadResponse extends Notification {}
