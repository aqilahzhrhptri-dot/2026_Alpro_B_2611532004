import subprocess
import os


def jalankan_git(perintah):
    """Menjalankan perintah Git."""
    hasil = subprocess.run(
        perintah,
        capture_output=True,
        text=True
    )

    if hasil.returncode != 0:
        print("\nTerjadi kesalahan:")
        print(hasil.stderr)
        return False

    if hasil.stdout:
        print(hasil.stdout)

    return True


def push_github():
    print("================================")
    print("       AUTO PUSH GITHUB")
    print("================================")

    # Memeriksa repository Git
    if not os.path.isdir(".git"):
        print("Folder ini bukan repository Git!")
        return

    # Memeriksa branch aktif
    hasil_branch = subprocess.run(
        ["git", "branch", "--show-current"],
        capture_output=True,
        text=True
    )

    if hasil_branch.returncode != 0:
        print("Gagal memeriksa branch.")
        print(hasil_branch.stderr)
        return

    branch = hasil_branch.stdout.strip()

    if not branch:
        print("Tidak ada branch aktif.")
        return

    print(f"\nBranch aktif: {branch}")

    # Memeriksa perubahan
    print("\nMemeriksa perubahan file...")

    if not jalankan_git(["git", "status", "--short"]):
        return

    # Menambahkan perubahan
    print("\nMenjalankan Git Add...")

    if not jalankan_git(["git", "add", "-A"]):
        return

    # Memeriksa perubahan yang siap di-commit
    hasil = subprocess.run(
        ["git", "diff", "--cached", "--quiet"]
    )

    if hasil.returncode == 0:
        print("\nTidak ada perubahan baru untuk di-commit.")
        return

    if hasil.returncode != 1:
        print("\nGagal memeriksa perubahan.")
        return

    # Meminta pesan commit
    pesan = input("\nMasukkan pesan commit: ").strip()

    if not pesan:
        print("Pesan commit tidak boleh kosong!")
        return

    # Menjalankan Commit
    print("\nMenjalankan Git Commit...")

    if not jalankan_git(
        ["git", "commit", "-m", pesan]
    ):
        return

    # Menjalankan Push
    print("\nMengirim perubahan ke GitHub...")

    hasil_push = subprocess.run(
        ["git", "push", "origin", branch],
        capture_output=True,
        text=True
    )

    if hasil_push.returncode != 0:
        print("\nPUSH GAGAL!")
        print(hasil_push.stderr)
        return

    if hasil_push.stdout:
        print(hasil_push.stdout)

    print("\n================================")
    print("       PUSH BERHASIL!")
    print(" File berhasil dikirim ke GitHub.")
    print("================================")


if __name__ == "__main__":
    push_github()