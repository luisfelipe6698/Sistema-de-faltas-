import { Request } from "express";

export function getSessionCookieOptions(req: Request) {
  const isProd = process.env.NODE_ENV === "production";
  const isSecure = isProd || req.protocol === "https";

  return {
    httpOnly: true,
    secure: isSecure,
    sameSite: isSecure ? ("none" as const) : ("lax" as const),
    path: "/",
  };
}

