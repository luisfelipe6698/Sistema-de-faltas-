import * as trpcExpress from "@trpc/server/adapters/express";
import jwt from "jsonwebtoken";
import * as db from "../db";
import { ENV } from "./env";

interface JwtPayload {
  userId: string;
  email: string;
}

export async function createContext({
  req,
  res,
}: trpcExpress.CreateExpressContextOptions) {
  async function getUser() {
    const token = req.cookies.eusouninja_session;
    if (!token) return null;

    try {
      const decoded = jwt.verify(token, process.env.JWT_SECRET || ENV.cookieSecret) as JwtPayload;
      const user = await db.getUser(decoded.userId);
      return user;
    } catch (error) {
      console.error("Error decoding token:", error);
      return null;
    }
  }

  const user = await getUser();

  return { req, res, user };
}

export type Context = Awaited<ReturnType<typeof createContext>>;

