export type ReviewImage = {
  url: string;
  height: number;
  width: number;
};

export type Review = {
  id: number;
  text: string;
  url: string;
  images: ReviewImage[];
};

export type Image = {
  id: number;
  location: string;
  image: string;
  height: number;
  width: number;
  uploadDate: Date;
  uploader: string;
  description: string;
};
