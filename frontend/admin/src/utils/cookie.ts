export const getCookie = (name: string) =>
  document.cookie.split('; ').reduce((r, v) => {
    const parts = v.split('=');
    return parts[0] === name ? decodeURIComponent(parts[1]) : r;
  }, '');

export const getCSRFToken = () => getCookie('csrftoken');
