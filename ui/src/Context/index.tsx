import { createContext, useState, useEffect } from 'react'
import { PortfolioDetails } from '../types';

export type AppState = {
  portfolios: PortfolioDetails[];
  hasPortfolio: boolean;
  currentUser: number;
  setCurrentUser: Function;
  users: any[];
  setUser: Function;
  createPortfolio: () => void;
  createUser: (username: string, password: string) => Promise<void>;
  fetchPortfolios: () => Promise<void>;
  fetchUsers: () => Promise<void>;
  addRemoveCurrency: (currency: any, add: boolean) => Promise<void>;
  availableCurrencies: any[];
}

export const AppContext = createContext<AppState>({
  portfolios: [],
  hasPortfolio: false,
  currentUser: 0,
  setCurrentUser: null as any,
  users: [],
  setUser: null as any,
  createPortfolio: null as any,
  createUser: null as any,
  fetchUsers: null as any,
  fetchPortfolios: null as any,
  addRemoveCurrency: null as any,
  availableCurrencies: []
})


export const AppProvider = ({ children }: React.PropsWithChildren) => {
  const [users, setUsers] = useState([]);
  const [currentUser, setCurrentUser] = useState(0);
  const [portfolios, setPortfolios] = useState<PortfolioDetails[]>([]);
  const [hasPortfolio, setHasPortfolio] = useState(false);
  const [availableCurrencies, setAvailableCurrencies] = useState<any[]>([]);

  useEffect(() => {
    fetchPortfolios();
    fetchUsers();
    fetch("http://localhost:8000/currency/")
        .then((response) => response.json())
        .then((data) => setAvailableCurrencies(data));
  }, []);

  useEffect(() => {
    if(currentUser > 0) {
      fetchPortfolios();
    }
  }, [currentUser])
  
  const createPortfolio = () => {
    setPortfolios([...portfolios, { currencies: [], portfolio: {} } as any as PortfolioDetails])
  }

  const createUser = async (username: string, password: string) => {
    await fetch(`http://localhost:8000/user/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          username: username,
          password: password
        })
    })

    await fetchUsers();
  }

  const fetchPortfolios = async () => {
    const res = await fetch(`http://localhost:8000/portfolio/${currentUser}/`)
    const json = await res.json();
    setHasPortfolio(json.length > 0)
    setPortfolios(json);
  }
  
  const fetchUsers = async () => {
    const res = await fetch(`http://localhost:8000/user/`)
    const json = await res.json();

    setUsers(json);
  }

  const addRemoveCurrency = async (currency: any, add: boolean) => {
    if(add) {
      if(hasPortfolio) {
        await fetch(`http://localhost:8000/portfolio/${portfolios[0].portfolio.id}/currencies/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            currencyId: currency.id
          })
        })
      }
      setPortfolios((portfolios) => {
        const newPortfolios = [...portfolios];
        newPortfolios[0].currencies.push(currency);
        return newPortfolios;
      })
    } else {
      if(hasPortfolio && portfolios[0].currencies.length <= 5) {
        alert("You must have at least 5 currencies in your portfolio")
        return;
      }

      await fetch(`http://localhost:8000/portfolio/${portfolios[0].portfolio.id}/currencies/`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          currencyId: currency.id
        })
      })

      setPortfolios((portfolios) => {
        const newPortfolios = [...portfolios];
        newPortfolios[0].currencies = newPortfolios[0].currencies.filter((c) => c.id !== currency.id);
        return newPortfolios;
      })
    }
  }

  return <AppContext.Provider value={{
    portfolios: portfolios,
    hasPortfolio: hasPortfolio,
    currentUser: currentUser,
    users: users,
    setUser: setCurrentUser,
    createPortfolio: createPortfolio,
    createUser: createUser,
    fetchPortfolios: fetchPortfolios,
    fetchUsers: fetchUsers,
    setCurrentUser: setCurrentUser,
    addRemoveCurrency: addRemoveCurrency,
    availableCurrencies: availableCurrencies
  }}>
    { children }
  </AppContext.Provider>
}
