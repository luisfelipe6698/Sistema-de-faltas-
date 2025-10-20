import { useEffect, useState } from "react";
import { trpc } from "../../lib/trpc";

export function useAuth() {
  const [user, setUser] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const { data, isLoading, error } = trpc.auth.me.useQuery();

  useEffect(() => {
    setLoading(isLoading);
    if (data) {
      setUser(data);
    } else if (error) {
      setUser(null);
    }
  }, [data, isLoading, error]);

  return { user, loading };
}

