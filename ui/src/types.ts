export type PortfolioDetails = {
  portfolio: {
    id: number;
    user_id: number;
    created_at: string;
    updated_at: string;
  },
  currencies: {
    id: number;
    name: string;
    symbol: string;
  }[]
}

export type UserList = {
  id: number;
  username: string;
}[];

export type User = {
  id: number;
  portfolio: {
    portfolio: {
      id: number;
      userId: number;
    },
    currencies: any[];
  };
}

