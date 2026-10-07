<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('alats', function (Blueprint $table) {
            $table->id();
            $table->string('kode_alat')->unique();
            $table->string('nama_alat');
            $table->string('jenis_alat');
            $table->string('merk')->nullable();
            $table->integer('tahun')->nullable();
            $table->foreignId('site_id')->constrained()->cascadeOnDelete();
            $table->enum('kondisi', ['Baik', 'Rusak Ringan', 'Rusak Berat']);
            $table->enum('status_operasional', ['Beroperasi', 'Maintenance', 'Tidak Aktif']);
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('alats');
    }
};
