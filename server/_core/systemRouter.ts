import { router, publicProcedure } from "./trpc";

export const systemRouter = router({
  healthcheck: publicProcedure.query(() => "ok"),
});

