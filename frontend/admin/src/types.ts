export type Image = {
  url: string;
  height: number;
  width: number;
};

export type Review = {
  id: number;
  text: string;
  url: string;
  images: Image[];
};
