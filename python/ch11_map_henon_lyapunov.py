from .dynamics.maps import compute_henon_lyapunov_exponents


def main():
    """Main function to compute and display Henon Lyapunov exponents."""
    h1, h2 = compute_henon_lyapunov_exponents()
    print(f"h_1 = {h1}")  # h_1 = 0.3391568093091681
    print(f"h_2 = {h2}")  # h_2 = -1.2565387259040743
    return h1, h2


if __name__ == "__main__":
    main()
