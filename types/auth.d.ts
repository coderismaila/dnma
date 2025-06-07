declare module "#auth-utils" {
  interface User {
    id: number;
    name: string;
    role: "user" | "manager" | "admin";
    email: string;
    image: string | null;
    areaOfficeId: number;
  }
}
export {};
